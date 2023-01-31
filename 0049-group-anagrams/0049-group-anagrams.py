from collections import defaultdict
class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        1. How to access strings inside a list?   ------> for loop in (len(strs))
        2. How to access character counts in those strings?  -----> Counter
        ** It is inside a list, so I have to iterate thru the list once to count the number of occurences in each string
        The Python defaultdict type behaves almost exactly like a regular Python dictionary, but if you try to access or modify a missing key, then defaultdict will automatically create the key and generate a default value for it. This makes defaultdict a valuable option for handling missing keys in dictionaries.
        for large datasets, it can also be a lot faster and more efficient. So, if speed is a concern for you, then you should consider using a defaultdict instead of a standard dict.
        
        """
        anagrams = defaultdict(list) #anything passed in: list, set, int creates {}, (<class 'list'/'set'/'int'> , {})
        for i in strs: 
            sortStr = sorted(i) #["a","e","t"]
            sorted_str = ''.join(sortStr) #"aet"
            # sorted_str = ''.join(sorted(i)) #https://www.scaler.com/topics/difference-between-sort-and-sorted-in-python/
            anagrams[sorted_str].append(i) #{'sorted keys': '[actal string values]'}
        return anagrams.values()