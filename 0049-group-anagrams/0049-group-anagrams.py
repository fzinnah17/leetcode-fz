class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        1. Create an empty dictionary to store anagram groups.
        2. For each word in the input:
           a. Sort the words and join them back together
           b. Check if it is already a key in map.
               I. If not, create a new entry as the key and a list containing as the value.
               II. If already in map, append `word` to the list of values associated with that key.
        3. After processing all words, return a list containing the values (lists of words) from the dictionary.
"""
        sMap = {} #key: sorted strings value = actual string
        for w in strs:
            sortStrs = "". join(sorted(w))
            # print(w)
            # print(sortStrs)
            # print()
            # eat  aet
            # tea  aet
            # tan  ant
            # ate  aet
            # nat  ant
            # bat  abt

            if sortStrs not in sMap:
                sMap[sortStrs] = [w]
            else:
                sMap[sortStrs]. append(w)
            # print(sMap)
            # {'aet': ['eat', 'tea', 'ate'], 'ant': ['tan', 'nat'], 'abt': ['bat']}
        return sMap.values()
        