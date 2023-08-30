class Solution(object):
    def longestConsecutive(self, nums):
        """
        the idea is to compare the given array with the set of it
        Pseudocode:
        1. have the numbers in the set in order for us to check the previous and the next value to increase the length SC: O(n)
        2. variable longest = 0
        3. for loop traversal in the given array: TC: O(n)
                
                a. start of the sequence:
                    if num - 1 not in set: 
                        variable length = 0
                        [the current number + updated length/next number if it is found in the set:
                            add length by 1] this condition runs until the sequence breaks 
                        as soon as the sequence breaks we have lengths that are being updated
                        maximum = max(length, longest maximum)
        4. we are done comparing between the array and the set so we can Return the longest     
        TC: O(n) SC: O(n)
        """
        numSet = set(nums)
        longest = 0
        for value in nums:
            if value - 1 not in numSet:
                length = 0
                while (value + length) in numSet:
                    length += 1
                longest = max(longest, length)
        return longest
        