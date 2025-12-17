def process_transactions(transactions):
    for amount in transactions:
        if amount < 0:
            continue     

        if amount == 9999:
            print("Stop Signal Received!")
            break         

        print("Processing:", amount)


transactions = [100, -50, 200, -20, 50, 9999, 300]
process_transactions(transactions)
