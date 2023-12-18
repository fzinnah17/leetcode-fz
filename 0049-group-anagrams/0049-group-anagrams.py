class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Arrays and Hashing: Store the times users have logged in inside an array and later retreive the recent logged in times
        
        For this problem,
        in the array the strings are added.
        I am retriving the strings in an array that are anagrams
        
        Pseudocode:
        1. iterate over the array
        2. count the frequency of each character of each string so e: 1, a: 1, t: 1 and have that inside the dictionary key = strs, val = frequency
        3. sort the dictionary values
        4. iterate over the dictionary values that are sorted
        5. whichever counts are matching, we can just add combine those characters as a string and append inside a list
        """
        result = {}
        for s in strs:
            char_count = {} #key = character, count = frequncy
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
        
        