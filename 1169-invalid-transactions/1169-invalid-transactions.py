class Solution:
    def invalidTransactions(self, transactions: List[str]) -> List[str]:
        invalid = []
        transactionList = defaultdict(list)
        
        for i in transactions:
            name, time, amount, city = i.split(",")
            transactionList[name].append([time, amount, city])

        for name, transactions in transactionList.items():
            for trans in transactions:
                t, a, c = trans
                if int(a) > 1000:
                    invalid.append(",".join([name, t, a, c]))
                else:
                    for other_trans in transactions:
                        ot, oa, oc = other_trans
                        if oc != c and abs(int(ot) - int(t)) <= 60:
                            invalid.append(",".join([name, t, a, c]))
                            break

        return invalid
