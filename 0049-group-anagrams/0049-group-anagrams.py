class Solution:
    def groupAnagrams(self, s: List[str]) -> List[List[str]]:
        """
        TC: O(nklogk) = O(n) + O(k) + O(klogk)
        SC: O(n)"""
        anagrams = {} #SC: O(n)
        
        for word in s: #TC: O(n) iterating each word in the string
            count = Counter(word) # TC: O(k) counting the frequency of each character
            countTuple = tuple(sorted(count.items())) #TC: O(klogk) sorting the counted items 
            if countTuple not in anagrams:
                anagrams[countTuple] = [word]
            else:
                anagrams[countTuple].append(word)
        return list(anagrams.values())
    
"""
        print(count):
            {'e': 1, 'a': 1, 't': 1}
            {'t': 1, 'e': 1, 'a': 1}
            {'t': 1, 'a': 1, 'n': 1}
            {'a': 1, 't': 1, 'e': 1}
            {'n': 1, 'a': 1, 't': 1}
            {'b': 1, 'a': 1, 't': 1}
        countTuple = sorted(count.items()): list -> [('a', 1), ('e', 1), ('t', 1)]
                                                    [('a', 1), ('e', 1), ('t', 1)]
                                                    [('a', 1), ('n', 1), ('t', 1)]
                                                    [('a', 1), ('e', 1), ('t', 1)]
                                                    [('a', 1), ('n', 1), ('t', 1)]
                                                    [('a', 1), ('b', 1), ('t', 1)]
                                            tuple -> list -> ()
        print(anagrams) outside of the for loop after checking all the words:
                    {
                    key : values
                    (('a', 1), ('e', 1), ('t', 1)) : ['eat', 'tea', 'ate'], 
                    (('a', 1), ('n', 1), ('t', 1)) : ['tan', 'nat'], 
                    (('a', 1), ('b', 1), ('t', 1)) : ['bat']
                    }
        countTuple = sorted(count.values()): [1, 1, 1]
                                             [1, 1, 1]
                                             [1, 1, 1]
                                             [1, 1, 1]
                                             [1, 1, 1]
                                             [1, 1, 1]
        countTuple = sorted(count.keys()): ['a', 'e', 't']
                                           ['a', 'e', 't']
                                           ['a', 'n', 't']
                                           ['a', 'e', 't']
                                           ['a', 'n', 't']
                                           ['a', 'b', 't']
"""