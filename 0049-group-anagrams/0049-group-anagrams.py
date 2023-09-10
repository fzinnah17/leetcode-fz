class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        strMap = {} #key = tuple(sorted char) value = [words]
        for word in s:
            sortedWord = "".join(sorted(word)) #aet,aet,ant,aet,ant,abt
            if sortedWord not in strMap:
                strMap[sortedWord] = [word]
            else:
                strMap[sortedWord].append(word)
        return list(strMap.values())
        