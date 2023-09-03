class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        Pseudocode:
        1. return variable: maxLen = 0
        2. two pointers to iterate the string -> left, right = 0, 0
        3. Initialize a Counter to store character frequencies
        4. while loop -> Ensure 'right' is within string bounds
                a. if right character count is still empty == 0 from the substring, then:
                        i. Update Counter for the current character by adding 1
                        ii. Move the 'right' pointer forward by 1
                        iii. find the maxLen = max(maxLen, right - left)  Update maxLen if needed
                b. if left character count is exceeding more than 1 from the substring, then:
                        i. Remove the character at 'left' from Counter
                        ii.Move the 'left' pointer forward by 1
            
        5. return maxLen
TC: O(n) SC: O(n)
        """
        maxLen = 0
        left, right = 0, 0
        charCount = Counter()
        
        while right < len(s):
            length = 0
            count = 0
            if charCount[s[right]] == 0:
                charCount[s[right]] += 1
                right += 1
                maxLen = max(maxLen, right - left)
            else:
                charCount[s[left]] -= 1
                left += 1
        return maxLen