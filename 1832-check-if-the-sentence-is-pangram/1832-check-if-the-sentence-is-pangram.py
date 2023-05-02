class Solution(object):
    def checkIfPangram(self, sentence):
        """
1. create a hashMap
2. add the keys and values to the hashMap by iterating the input
3. iterate over the lowercase letters(or whatever the question requires)
    a. if that specific character is in the hashMap, then return True
    b. Or return False
Yes we can compare a list of characters with a dictionary containing key-value pairs. One way to check if all the characters in the list are present in the dictionary is to iterate over the list of characters and check if each character exists as a key in the dictionary. 
        """
        hashMap = {}
        for l in sentence:
            if l in hashMap:
                hashMap[l] += 1
            hashMap[l] = 1
        for i in range(97,123):
            if chr(i) not in hashMap:
                return False
        return True
        #TC: O(n) SC: O(n)
                
                
                
        
        