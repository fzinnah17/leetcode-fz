class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        # s.sort()
        sMap = {}
        for i in s:
            # print(i)
            #each i
            w = "".join(sorted(i))
            #sort each i and make it w
            # print(w)
            if w not in sMap:
                #if that w not in the map then add otherwise append
                sMap[w] = [i]
            else:
                sMap[w].append(i)
        return sMap.values()
        # print(s)
        