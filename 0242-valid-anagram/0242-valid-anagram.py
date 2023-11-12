class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sMap = defaultdict(int)
        tMap = defaultdict(int)
        # print(sMap, tMap)
        for i in range(len(s)):
            sMap[s[i]] += 1
        for i in range(len(t)):
            tMap[t[i]] += 1
        #print(sMap, tMap)
        if sMap == tMap:
            return True
        return False