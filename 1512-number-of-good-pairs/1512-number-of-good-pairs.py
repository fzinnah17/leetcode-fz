class Solution(object):
    def numIdenticalPairs(self, nums):
        """
        Pseudocode:
        1. Initialize output to 0
        2. Two pointers:
            i = 0,
        3. Iterate over the list:(while loop) to check which numbers are the same
            j = i + 1 *****
            Another while loop to check:
                if nums[i] == nums[j]:
                    output += 1
                j += 1
        4. i += 1
            we have to keep on going till we exceed the boundary 
            TC: O(n^2) because it uses nested loops. The outer loop runs (n - 1) times and the inner loop runs (n - i) times
            SC: O(1) constant time as we did not use any additional data structure to grow with the input size
        """
        output = 0
        i = 0
        while i < len(nums)-1:
            j = i + 1
            while j < len(nums):
                if nums[i] == nums[j]:
                    output += 1
                j += 1
            i += 1
        return output
    
    """1. Initialize output to 0
2. Initialize i to 0
3. While i is less than len(nums) - 1:
   4. Initialize j to i + 1
   5. While j is less than len(nums):
      6. If nums[i] is equal to nums[j]:
         7. Increment output by 1
      8. Increment j by 1
   9. Increment i by 1
10. Return output
"""
        
        