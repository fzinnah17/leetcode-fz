class Solution(object):
    def checkInclusion(self, s1, s2):
        """
1. what it means for two strings to be permutation of each other?: Any permutation of any of these strings has to be present in the other string.
2. TC: O(nlogn) or O(n)[if some space is used]
3. Both strings must have same character frequencies, if one is permutation of another. Which data structure should be used to store frequencies?: Counter
EDGE CASES:
            a. if s1 is found in s2: True
            b. length s2 < length s1: False
            c. length same, both string count same: True
        """
        stringOne = Counter(s1)
        stringTwo = Counter(s2)
        
        for i in range(len(s2) - len(s1) + 1): #how is it guaranteed that the last two characters of s2 wont have the permutation?
            if stringOne == Counter(s2[i:i+len(s1)]):
                return True
        return False
            
        