class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        strMap = {} #key = tuple(sorted char) value = [words]
        for word in s:
            sortedTuple = tuple(sorted(word))
            if sortedTuple not in strMap:
                strMap[sortedTuple] = [word]
            else:
                strMap[sortedTuple].append(word)
        return list(strMap.values())
        