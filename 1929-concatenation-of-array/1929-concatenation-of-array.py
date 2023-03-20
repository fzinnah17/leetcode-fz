class Solution(object):
    def getConcatenation(self, nums):
        """
        To solve this problem, I need to write a function that returns an array  of length 2n.
        The given array is length of n, but the ans will have the elements, but twice
        """
        output = []
        for i in nums:
            output.append(i)
        for j in nums:
            output.append(j)
        return output
        