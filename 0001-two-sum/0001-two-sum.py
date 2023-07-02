class Solution(object):
    def twoSum(self, nums, target):
        """
TC & SC: O(N)
        """
        output = []
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                currSum = nums[i] + nums[j]
                if currSum == target:
                    output.append(i)
                    output.append(j)
        return output
                    
                