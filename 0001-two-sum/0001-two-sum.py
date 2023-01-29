class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        #[2,3,4,5,7] target = 11
        # t
        #{}
        
        hashMap = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in hashMap:
                return [hashMap[diff],i]
            hashMap[nums[i]] = i
            
            
            
        
        