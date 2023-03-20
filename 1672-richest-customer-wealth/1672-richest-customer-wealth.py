class Solution(object):
    def maximumWealth(self, accounts):
        """
        Psedu-code:
        1. traverse the row one by one
        2. As traversing, update the sum (initial = 0)
        3. after each row is calculated, keep the maximum.
        4. for next row, follow the steps from earlier, but don't change sum if the currVal is NOT > than prevVal
        5. return the sum
        TC: O(n+m) SC: O(1) 
        """
        ans = 0
        for i in range(len(accounts)):
            wealth = 0
            for j in range(len(accounts[i])):
                wealth += accounts[i][j]
                if wealth > ans: 
                    ans = wealth
        return ans
                
                
        