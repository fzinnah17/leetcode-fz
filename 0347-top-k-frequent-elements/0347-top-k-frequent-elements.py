class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numsMap = {} #key = nums[i], value: count
        
        for i in range(len(nums)):
            if nums[i] not in numsMap:
                numsMap[nums[i]] = 1
            else:
                numsMap[nums[i]] += 1
        # print(numsMap) 
        # print()
        sortedMap = sorted(numsMap.items(), key = lambda x : x[1], reverse = True)
        """
        Now I want to return the 'k' keys of the tuple"""
        # print(sortedMap[:k])
        # print()
        res = [n[0] for n in sortedMap[:k]]
        # print(res)
        return res
        """
        Time: O(n) to create the map, sort the map is O(logn), O(n) to find the first k time repeated items = O(nlogn)
        Space: O(n) for creating a map
        """