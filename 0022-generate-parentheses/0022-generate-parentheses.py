class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        TC: The worst-case scenario is when you have to generate all possible combinations of parenthesis. This is exponential and is approximately O(2^(2n)/sqrt(n)), based on the nth Catalan number. This is because there are 2^(2n) total sequences for n pairs of parentheses, but only the nth Catalan number of them are valid.
        SC: The space required will also be exponential in the worst case, which is the number of valid sequences. So, O(2^(2n)/sqrt(n)).
"""
        res = []
        
        q = deque([('',0,0)])
        
        while q:
            currStr, currOpen, currClose = q.popleft()
            if currOpen == n and currClose == n:
                res.append(currStr)
            else:
                if currOpen < n:
                    q.append((currStr + '(', currOpen + 1, currClose))
                if currOpen > currClose:
                    q.append((currStr + ')', currOpen, currClose + 1))

        return res
        