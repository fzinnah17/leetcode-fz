class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numDict = {}
        
        for i in range(len(nums)):
            comp = target - nums[i]
            
            if comp not in numDict:
                numDict[nums[i]] = i
            else:
                return [i, numDict[comp]]
        
        