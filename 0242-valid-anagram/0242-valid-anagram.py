class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap ={} #key = character aka value
        tMap = {}
        
        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = 1
            else:
                sMap[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in tMap:
                tMap[t[i]] = 1
            else:
                tMap[t[i]] += 1
        """
        {'a': 3, 'n': 1, 'g': 1, 'r': 1, 'm': 1}

        {'n': 1, 'a': 3, 'g': 1, 'r': 1, 'm': 1}
"""
        
        if sMap != tMap:
            return False
        return True
                
                