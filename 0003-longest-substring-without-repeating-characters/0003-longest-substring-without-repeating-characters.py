class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Pseudocode:
        1. variable to return max
        2. two pointers: left and right
        3. each character count using Counter creation: O(n) but accessing O(1)
        4. while loop: right cant surpass the length of s
            a. if the right character count = 0:
                character count of right += 1
                right += 1
                max = max(max, right - left)
            b. else:
                character count of left -= 1
                left += 1
        5. return the variable
        TC: O(n) SC: O(1)
        """
        maxLen = 0
        left, right = 0,0
        charCount = Counter()
        
        while right < len(s):
            if charCount[s[right]] == 0:
                charCount[s[right]] += 1
                right += 1
                maxLen = max(maxLen, right - left)
            else:
                charCount[s[left]] -= 1
                left += 1
        return maxLen
        
        
        