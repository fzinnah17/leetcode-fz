class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = re.sub(r'[^a-zA-Z0-9]', '', s)
        s = s.lower()
        # newStr = s[::-1]
        if s == s[::-1]:
            return True
        return False
        
        # newStreverse = newStr[::-1]
        
#         counts = Counter(s)
#         newStr = s[::-1]
#         countNew = Counter(newStr)
        
#         if counts == countNew:
#             return True
#         return False
        # print(counts)
        # print(countNew)
        
        
        