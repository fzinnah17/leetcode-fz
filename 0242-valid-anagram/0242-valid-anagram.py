class Solution(object):
    from collections import Counter
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        A Counter is a dict subclass for counting hashable objects. It is a collection where elements are stored as dictionary keys and their counts are stored as dictionary values.
        """
        """use counter for both and check if it is equal. If so, return True"""
        str1 = collections.Counter(s)
        str2 = collections.Counter(t)
        
        if str1 == str2:
            return True
        return False
        
        # print(str1)
        # print(str2)
        
        
        
        