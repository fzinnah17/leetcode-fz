class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsMap = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp not in numsMap:
                numsMap[nums[i]] = i
            else:
                return [i,numsMap[comp]]
        #  Time: O(n) Space: O(n)
        