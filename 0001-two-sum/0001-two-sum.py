class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nMap ={} #key = v, value = index
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp not in nMap:
                nMap[nums[i]] = i
            else:
                return [i, nMap[comp]]
        
        