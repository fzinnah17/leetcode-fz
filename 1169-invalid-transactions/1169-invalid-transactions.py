class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        transactionList = defaultdict(list)
        
        for i in transactions:
            name, time, amount, city = i.split(",")
            transactionList[name].append([time,amount,city]) #hashmap[key] = [value]
        """{'alice': [
                     ['20', '800', 'mtv'], 
                     ['50', '100', 'beijing']
                     ]}
"""
        
        for j in range(len(transactions)):
            name, time, amount, city = transactions[j].split(",")
            """alice 20 800 mtv
               alice 50 100 beijing"""
            if int(amount) > 1000:
                invalid.append(transactions[j])
            else:
                for trans in transactionList[name]:
                    t, a, c = trans
                    if c != city and abs(int(t)-int(time)) <= 60:
                        invalid.append(transactions[j])
                        break
        return invalid
    """TC: O(n^2) SC: O(n)"""
                
                
                
        
        