class Solution(object):
    def removeAnagrams(self, words):
        """
        Pseudocode:
            1. We can start by using a while loop
                a. if counter(words[i-1]) == counter(words[i]):
                    delete words[i] even tho sometimes changing/deleting from list may lead to unexpected results, so the safer approach is to create a new list.
                b. else:
                    increment the pointer i to the words[i]
                    and repeat the process
            2. return the list at the end
            TC: O(n) SC: O(n) as I am using counters that creates frequency tables
        """
        i = 1
        while i < len(words):
            if Counter(words[i-1]) == Counter(words[i]):
                del words[i]
            else:
                i += 1
        return words
        