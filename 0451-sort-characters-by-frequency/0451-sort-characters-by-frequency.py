class Solution(object):
    def frequencySort(self, s):
        """
        Pseudocode:
        1. Use counter to store how many times each character has appeared in decreasing order
        2. traverse the hashMap created by the counter
        3. create a string from the most to least characters from that hashMap
        TC & SC : O(n)
        """
        hashMap = Counter(s).most_common()
        characters = []
        result = ""
        for c in hashMap:
            characters.append(c)
        for key,val in characters:
            letters = key * val
            result += letters
        return result
        
        """print(characters):
            [(u'i', 16)]
            [(u'i', 16), (u's', 16)]
            [(u'i', 16), (u's', 16), (u'p', 8)]
            [(u'i', 16), (u's', 16), (u'p', 8), (u'm', 4)]
            
            print(letters)
            iiiiiiiiiiiiiiii
            ssssssssssssssss
            pppppppp
            mmmm"""
        