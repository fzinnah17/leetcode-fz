class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        """
        res = 0
        right = 0
        left = 0
        stringSet = set()

        while right < len(s):
            if s[right] not in stringSet:
                stringSet.add(s[right])
                res = max(res, right - left + 1)
                right += 1
            else:
                stringSet.remove(s[left])
                left += 1
        return res
        