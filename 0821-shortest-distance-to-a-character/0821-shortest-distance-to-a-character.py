class Solution:
    def shortestToChar(self, S, C):
        myList = [i for i,letter in enumerate(S) if letter == C]
        result = []
        for i in range(len(S)):
            min_pos = []
            for j in myList:
                min_pos.append(abs(j-i))
            result.append(min(min_pos))
        return result