class Solution(object):
    def longestConsecutive(self, nums):
        """
        """
        ans = 0
        hashSet = set(nums)

        for n in nums:
            if n - 1 not in hashSet:
                curr = n
                streak = 1
                while curr + 1 in hashSet:
                    curr += 1
                    streak += 1
                ans = max(ans, streak)
        return ans
        