class Solution(object):
    def groupAnagrams(self, strs):
        anagrams = defaultdict(list) #anything passed in: list, set, int creates {}, (<class 'list'/'set'/'int'> , {})
        for i in strs: 
            sortStr = sorted(i) #["a","e","t"]
            sorted_str = ''.join(sortStr) #"aet"
            # sorted_str = ''.join(sorted(i)) #https://www.scaler.com/topics/difference-between-sort-and-sorted-in-python/
            anagrams[sorted_str].append(i) #{'sorted keys': '[actal string values]'}
        return anagrams.values()