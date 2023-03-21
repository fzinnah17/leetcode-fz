class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        """
        Psedu-code:
        1. Create a list [], Initial sum 0
        2. Traverse the array
                a. As traversing, add the nums[i] with the sum
                b. add the sum in the list
        3. return a list with all the sum
        TC and SC: O(n)"""
        output = []
        elSum = 0
        for i in range(len(nums)):
            elSum += nums[i]
            output.append(elSum)
        return output
        
        """But how to optimize the solution? TC: O(n) SC: O(1)
        for i in range(1,len(nums)):
            nums[i] += nums[i-1]
        return nums
        """