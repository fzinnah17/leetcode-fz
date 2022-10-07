class Solution(object):
    def frequencySort(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        new_string = ''
        hashMap = {}
        
        for index, character in enumerate(s):
            if character not in hashMap:
                hashMap[character] = 1 #think of hashMap[character] as count
            else:
                hashMap[character] += 1
        #here we are sorting in decreasing order -> reverse = True
        #we are taking the filled hashMap and lambda has a variable and body has count[how many times the char has occured]
        char_sorted = sorted(hashMap, key= lambda count: hashMap[count], reverse = True)
        
        for index, character in enumerate(char_sorted):
            new_string += character*hashMap[character] #hashMap[character] = hashMap[count] from the char_sorted function
        return new_string
    #TC: O(n), SC: O(n)            
        