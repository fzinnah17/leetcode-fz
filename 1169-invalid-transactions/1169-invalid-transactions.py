class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        
        # Map to store transactions grouped by name
        transactions_by_name = {}
        
        # Set to store indices of invalid transactions
        invalid_transaction_indices = set()
        
        # Step 1: Group transactions by name
        current_index = 0
        while current_index < len(transactions):
            transaction = transactions[current_index]
            name, time, amount, city = transaction.split(',')
            
            # If the name is not in the map, add it with an empty list
            if name not in transactions_by_name:
                transactions_by_name[name] = []
                
            # Append the current transaction to the list for the specific name
            transactions_by_name[name].append((current_index, int(time), int(amount), city))
            
            # Move to the next transaction
            current_index += 1

        # Step 2: Check for invalid transactions
        for name, transactions_for_name in transactions_by_name.items():
            first_transaction_index = 0
            while first_transaction_index < len(transactions_for_name):
                idx1, time1, amount1, city1 = transactions_for_name[first_transaction_index]
                
                # Condition 1: Check for amount greater than 1000
                if amount1 > 1000:
                    invalid_transaction_indices.add(idx1)
                    
                second_transaction_index = 0
                while second_transaction_index < len(transactions_for_name):
                    idx2, time2, amount2, city2 = transactions_for_name[second_transaction_index]
                    
                    # Condition 2: Check for time difference and different cities
                    if first_transaction_index != second_transaction_index and abs(time1 - time2) <= 60 and city1 != city2:
                        invalid_transaction_indices.add(idx1)
                        invalid_transaction_indices.add(idx2)
                    
                    # Move to the next transaction
                    second_transaction_index += 1
                
                # Move to the next transaction
                first_transaction_index += 1
            
        # Step 3: Collect invalid transactions
        invalid_transactions = []
        for idx in invalid_transaction_indices:
            invalid_transactions.append(transactions[idx])
            
        return invalid_transactions
