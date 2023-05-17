class Solution(object):
    def twoSum(self, nums, target):
        """
        TC: O(n) SC: O(n)
        Pseudocode:
        1. Initialize an empty dictionary
        2. pointer i = 0
        3. While loop to traverse the nums array
        4. check if the curr is in the dictionary
            if it is, then return the indices [dictionary[curr], i]
        5. If not, then add the indices to the dictionary
        6. incrememnt the i
        7. return [] if none can be found
        """
        i = 0
        hashMap = {}
        while i < len(nums):
            curr = target - nums[i]
            if curr in hashMap:
                return [hashMap[curr], i]
            hashMap[nums[i]] = i
            i += 1
        return []
        