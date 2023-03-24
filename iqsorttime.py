import csv

# Define the account names
account_names = ["Anne", "Bob", "Clair"]

# Loop through each account name
for account_name in account_names:
    # Open the CSV file
    with open("data.csv", "r") as file:
        # Create a CSV reader object
        reader = csv.DictReader(file)
        
        # Create a list to hold the transactions for this account
        account_transactions = []
        
        # Loop through each row in the CSV file
        for row in reader:
            # Check if the account name matches
            if row["AccountName"] == account_name:
                # Create a dictionary for this transaction
                transaction = {"TransactionNumber": row["TransactionNumber"], "Date": row["Date"], "Amount": row["Amount"]}
                
                # Add the transaction to the list
                account_transactions.append(transaction)
                
        # Sort the transactions by date
        account_transactions.sort(key=lambda x: datetime.datetime.strptime(x["Date"], "%d/%m/%Y"))
        
        # Create a filename for this account's report
        filename = f"{account_name}_report.csv"
        
        # Open the file for writing
        with open(filename, "w", newline="") as file:
            # Create a CSV writer object
            writer = csv.writer(file)
            
            # Write the header row
            writer.writerow(["TransactionNumber", "Date", "Amount", "Remark"])
            
            # Loop through each transaction for this account
            for transaction in account_transactions:
                # Write the transaction to the CSV file
                writer.writerow([transaction["TransactionNumber"], transaction["Date"], transaction["Amount"], row.get("Remark", "")])
                
print("Reports created successfully.")
