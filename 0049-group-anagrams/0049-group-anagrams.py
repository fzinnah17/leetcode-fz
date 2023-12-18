class Solution:
    def groupAnagrams(self, strs):
        result = {}
        for s in strs:
            char_count = {}  # key = character, count = frequency
            for ch in s:
                if ch not in char_count:
                    char_count[ch] = 1
                else:
                    char_count[ch] += 1
            key = tuple(sorted(char_count.items()))
            
            if key not in result:
                result[key] = [s]  # Initialize a list for this character count
            else:
                result[key].append(s)
            
        groupedAnagrams = list(result.values())
        
        return groupedAnagrams
