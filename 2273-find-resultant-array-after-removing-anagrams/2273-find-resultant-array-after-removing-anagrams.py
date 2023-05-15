class Solution(object):
    def removeAnagrams(self, words):
        """
        Pseudocode:
            1. We can start by using a for loop
                a. if counter(words[i-1]) == counter(words[i]):
                    delete words[i]
                    but then if I delete it first, then how do I get to the next string of the list?
                b. else:
                    increment the pointer i to the words[i]
                    and repeat the process
            2. return the list at the end
            TC: O(n) SC: O(1) as I am trying to delete the strings from the list.
        """
        i = 1
        while i < len(words):
            if Counter(words[i-1]) == Counter(words[i]):
                del words[i]
            else:
                i += 1
        
        return words
                
        