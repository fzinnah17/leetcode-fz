class Solution(object):
    def maxSubArray(self, nums):
        '''My approach: if at any point sum returns - number we can just disregard that and keep it 0 to add later. If the value is + then we can add it our sum and update maximum sum.'''
        maxSofar = nums[0]
        currSum = 0
        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i
            maxSofar = max(maxSofar,currSum)
        return maxSofar

        # for i in range(1,len(nums)):
        #     nums[i] = max(nums[i],nums[i]+nums[i-1])
        # return max(nums)

        """
        Using Kadnae's Algorithm
        """
        # maxCurrindex = nums[0]
        # maxSofar = nums[0]
        
        # for curr_index in nums[1:]:
        #     maxCurrindex = max(maxCurrindex+curr_index, curr_index)
        #     maxSofar = max(maxSofar, maxCurrindex)
        # return maxSofar
        
        
        
        