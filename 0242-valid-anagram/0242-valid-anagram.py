class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sMap = defaultdict(int)
        # tMap = defaultdict(int)
        sMap = {}
        tMap = {}
        for i in range(len(s)):
            if s[i] not in sMap:
                sMap[s[i]] = 1
            sMap[s[i]] += 1
        for i in range(len(t)):
            if t[i] not in tMap:
                tMap[t[i]] = 1
            tMap[t[i]] += 1
        #print(sMap, tMap)
        if sMap == tMap:
            return True
        return False