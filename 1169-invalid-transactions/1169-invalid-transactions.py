class Solution:
    def invalidTransactions(self, trans: List[str]) -> List[str]:
        
        hmap = {}
        invalid_indices = set()
        
        for i, t in enumerate(trans):
            name, time, amount, city = t.split(',')
            if name not in hmap:
                hmap[name] = []
            hmap[name].append((i, int(time), int(amount), city))

#         alice -> [[1, 20, 800, mtv], []]
        for name, transactions in hmap.items():
            for i, (idx1, time1, amount1, city1) in enumerate(transactions):
                
                if amount1 > 1000:
                    invalid_indices.add(idx1)
                    
                for j, (idx2, time2, amount2, city2) in enumerate(transactions):
                    if i != j and abs(time1 - time2) <= 60 and city1 != city2:
                        invalid_indices.add(idx1)
                        invalid_indices.add(idx2)
            
        return [trans[i] for i in invalid_indices]