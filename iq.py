import csv
from datetime import datetime

with open('data.csv', mode='r') as csv_file:
    for i in range(2):
        next(csv_file)
    csv_reader = csv.DictReader(csv_file, fieldnames=['TransactionNumber', 'Date', 'AccountName', 'Amount', 'Remark'])
    transactions = list(csv_reader)

account_transactions = {}
for transaction in transactions:
    account_name = transaction['AccountName']
    if account_name not in account_transactions:
        account_transactions[account_name] = []
    account_transactions[account_name].append(transaction)

transactions_sorted = sorted(transactions, key=lambda x: x['Date'][3:5]+x['Date'][0:2]+x['Date'][6:])

for account_name, transactions in account_transactions.items():
    transactions = [t for t in transactions]

    with open(f'{account_name}.csv', mode='w', newline='') as csv_file:
        fieldnames = ['TransactionNumber', 'Date', 'Amount', 'Remark']
        csv_writer = csv.writer(csv_file)
        csv_writer.writerow(['Account Name',account_name])
        csv_writer.writerow(fieldnames)
        
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        for transaction in transactions:
            csv_writer.writerow({
                'TransactionNumber': transaction['TransactionNumber'],
                'Date': transaction['Date'],
                'Amount': transaction['Amount'],
                'Remark': transaction['Remark']
            })
