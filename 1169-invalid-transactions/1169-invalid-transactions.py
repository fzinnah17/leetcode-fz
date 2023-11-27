class Solution:
    def invalidTransactions(self, trans: List[str]) -> List[str]:
        
        hmap = {}
        invalid_indices = set()
        
        i = 0
        while i < len(trans):
            t = trans[i]
            name, time, amount, city = t.split(',')
            
            if name not in hmap:
                hmap[name] = []
                
            hmap[name].append((i, int(time), int(amount), city))
            i += 1

        for name, transactions in hmap.items():
            j = 0
            while j < len(transactions):
                idx1, time1, amount1, city1 = transactions[j]
                
                if amount1 > 1000:
                    invalid_indices.add(idx1)
                    
                k = 0
                while k < len(transactions):
                    idx2, time2, amount2, city2 = transactions[k]
                    
                    if j != k and abs(time1 - time2) <= 60 and city1 != city2:
                        invalid_indices.add(idx1)
                        invalid_indices.add(idx2)
                    
                    k += 1
                
                j += 1
            
        invalid_transactions = []
        for i in invalid_indices:
            invalid_transactions.append(trans[i])
        return invalid_transactions
