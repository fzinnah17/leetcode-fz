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
        currSum = 0
        for i in range(len(nums)):
            currSum += nums[i]
            output.append(currSum)
        return output