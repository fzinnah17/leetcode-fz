class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        Brute Force: We can check every single substring and therefore it will create O(n^2) time complexity
        """
        left = 0
        right = 0
        maxLen = 0
        hashMap = {}
        while right < len(s):
            if s[right] in hashMap:
                hashMap[s[right]] += 1
            else:
                hashMap[s[right]] = 1
            
            windowSize = right - left + 1
            if (windowSize - max(hashMap.values())) <= k:
                maxLen = max(maxLen, windowSize)
            else:
                # if (windowSize - max(hashMap.values())) > k:
                hashMap[s[left]] -= 1
                    # if hashMap[s[left]] == 0:
                    #     del hashMap[s[left]]
                left += 1
            right += 1
            # maxLen = max(maxLen, windowSize)
            
        return maxLen
                