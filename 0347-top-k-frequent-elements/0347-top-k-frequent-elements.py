from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        i can check the occurences using counter
        if counter elements >= k, then return those values
        """
        n = collections.Counter(nums)
        res =[]
        for i in n.most_common(k):
            res.append(i[0])
        return res
            
        #print(n) #Counter({1: 3, 2: 2, 3: 1})
        #if val> k:
            #return that val