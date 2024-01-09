class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {}
        
        for i in range(len(nums)):
            if nums[i] not in numsMap:
                numsMap[nums[i]] = 1
            else:
                numsMap[nums[i]] += 1
        
        sortedMap = sorted(numsMap.items(), key = lambda x : x[1], reverse = True)
        return [i[0] for i in sortedMap[:k]]
        # print(numsMap)
        