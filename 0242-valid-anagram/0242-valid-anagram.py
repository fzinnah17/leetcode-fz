class Solution(object):
    def isAnagram(self, s, t):
        """
        Counter is a frequency table. It is an object. 
        Key       :     Values
        char/num  :     Frequency
        """
        s = collections.Counter(s)
        t = collections.Counter(t)
        if s == t:
            return True
        return False
        