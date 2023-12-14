class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        # Sort the list first to handle the sequence in an ordered manner
        nums.sort()

        # Calculate the initial range of the array
        originalRange = nums[-1] - nums[0]
        
        # Initialize the result with the original range
        result = originalRange

        # Iterate through the array
        for i in range(len(nums) - 1):
            # Calculate lower and upper bounds at the current index
            lowerBoundAtCurrent = nums[i] - k
            upperBoundAtCurrent = nums[i] + k

            # Calculate the potential new minimum and maximum of the array
            potentialNewMin = min(nums[0] + k, nums[i + 1] - k)
            potentialNewMax = max(nums[-1] - k, upperBoundAtCurrent)

            # Calculate the new range and update the result if it's smaller
            newRange = potentialNewMax - potentialNewMin
            result = min(result, newRange)

        return result
