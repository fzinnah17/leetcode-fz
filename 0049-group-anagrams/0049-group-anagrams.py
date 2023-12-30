class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. Iterate over the string to create a map
        2. """
        resMap = {}
        for s in strs:
            words = "".join(sorted(s))
            if words not in resMap:
                resMap[words] = [s]
                # print(resMap)
            else:
                resMap[words].append(s)
        # print(resMap)
        return list(resMap.values())
        