class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def helper(current, leftPar, rightPar):
            if len(current) == 2*n:
                result.append(current)
                return
            if leftPar < n:
                helper(current + "(", leftPar + 1, rightPar)
            if rightPar < leftPar:
                helper(current + ")", leftPar, rightPar + 1)
        helper("", 0, 0)
        return result
        