class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        sMap = {}
        longest = 0
        max_count = 0
        l, r = 0, 0
        
        while r < len(s):
            if s[r] not in sMap:
                sMap[s[r]] = 1
            else:
                sMap[s[r]] += 1
            max_count = max(max_count, sMap[s[r]])

            if (r - l + 1 - max_count) > k:
                sMap[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

            r += 1  # Increment the right pointer

        return longest
