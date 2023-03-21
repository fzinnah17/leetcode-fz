class Solution(object):
    def diStringMatch(self, s):
        """
TC: O(n) SC: O(n)
        """
        i = 0
        d = len(s)
        output = []
        for el in s:
            if el == "I":
                output.append(i)
                i += 1
            else:
                output.append(d)
                d -= 1
        output.append(i)
        return output
                