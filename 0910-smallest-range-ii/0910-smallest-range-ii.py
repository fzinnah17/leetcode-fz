class Solution:
    def smallestRangeII(self, nums: List[int], k: int) -> int:
        # Sort the list first to handle the sequence in an ordered manner
        nums.sort()

        # Calculate the initial range of the array
        originalRange = nums[-1] - nums[0]
        
        # Initialize the result with the original range
        result = originalRange

        # Iterate through the array
        for i in range(len(nums)):
            # When i is the last index, break the loop as we can't use nums[i + 1]
            if i == len(nums) - 1:
                break

            # Calculate the potential new min and max
            newMin = min(nums[0] + k, nums[i + 1] - k)
            #nums[i] < nums[i + 1] that's why minimize the i + 1 value
            newMax = max(nums[i] + k, nums[-1] - k)

            # Calculate the new range and update the result if it's smaller
            result = min(result, newMax - newMin)

        return result
