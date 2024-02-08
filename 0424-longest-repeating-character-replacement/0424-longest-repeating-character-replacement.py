from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        """
        count how many times each character is present using defaultdict not counter
        have pointers
        if l != r: and as long as k exists and != 0: replace the character with the highest character and
        calculate the length
        return the maximum length
        """
        strDict = defaultdict(int)
        l, r = 0, 0
        maxFreq = 0
        output = 0
        
        while r < len(s):
            strDict[s[r]] += 1
            maxFreq = max(maxFreq, strDict[s[r]])
            
            if r - l + 1 - maxFreq > k:
                strDict[s[l]] -= 1
                l += 1
            
            output = max(output, r - l + 1)
            r += 1
        
        return output
