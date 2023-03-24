import csv
from datetime import datetime

# read transactions from data.csv file
with open('data.csv', mode='r') as csv_file:
    for i  in range(2):
        next(csv_file)
    csv_reader = csv.DictReader(csv_file, fieldnames=['TransactionNumber', 'Date', 'AccountName', 'Amount', 'Remark'])
    transactions = list(csv_reader)

# ทำ dict เก็บข้อมูล
account_transactions = {}
for transaction in transactions:
    account_name = transaction['AccountName']       #สร้าง key ใน accname
    if account_name not in account_transactions:
        account_transactions[account_name] = []     #key =value
        account_transactions[account_name].append(transaction)
    else:
        account_transactions[account_name].append(transaction)
transactions_sorted = sorted(transactions, key=lambda x: x['Date'][3:5]+x['Date'][0:2]+x['Date'][6:])
# create a report for each account owner
for account_name, transactions in account_transactions.items():
    # filter out transactions with empty remarks
    transactions = [t for t in transactions ]
    # sort transactions by date
    # transactions = sorted(transactions, key=lambda t: t['Date'])
    
    # write report to CSV file
    with open(f'{account_name}.csv', mode='w', newline='') as csv_file:
        fieldnames = ['TransactionNumber', 'Date', 'Amount', 'Remark']
        csv_writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
        csv_writer.writeheader()
        for transaction in transactions:
            csv_writer.writerow({
                'TransactionNumber': transaction['TransactionNumber'],
                'Date': transaction['Date'],
                'Amount': transaction['Amount'],
                'Remark': transaction['Remark']
            })
