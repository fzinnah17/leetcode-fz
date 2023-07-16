class Solution(object):
    def romanToInt(self, s):
        """
        Pseudocode:
        1. Initialize variables: currSum = 0
        2. create hash table using {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
                                    here, index/ch = key, value = value
        3. create pointers to iterate the string
        4. Iterate through the string given so that we can do pairwise subtraction. It involves subtracting two values from a string at a time and forming a new string with the results.:
                if the characters are present in the dictionary:
                    if the current character value >= the next character value:
                        currSum += current character
                        left += 1
                        right += 1
                    else:
                        currSum += next character value - current character value
                        increment the left pointer
                        increment the right pointer
                        so that two characters are skipped
        5. For the odd cases,
            if any single character remains/ left < len(s) as we will only have the left pointer:
                add the value of that left pointer to the output
                currSum += dict(left value)
        6. Return the output
        TC: O(n) SC: O(n)
        """
        currSum = 0
        left = 0
        right = left + 1
        romanDict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        while left < len(s) - 1:
            if s[left] in romanDict and s[right] in romanDict:
                if romanDict[s[left]] >= romanDict[s[right]]:
                    currSum += romanDict[s[left]]
                    left += 1
                    right = left + 1
                else: #s[left] < s[right] 
                    currSum += romanDict[s[right]] - romanDict[s[left]]
                    #C M     to          X                          C
                    #l r           l = r + 1(old right)       r = l + 1(new left)
                    left = right + 1
                    right = left + 1
        if left < len(s): #when there is a single character left after the loop has finished.
            currSum += romanDict[s[left]]

        return currSum
    
    """           
        CMXCIV
        (M- C) = (1000 - 100) = 900 
        + 
        (C - X) = (100 - 10) = 90 
        + 
        (V - I) = (5 - 1) = 4 
        = 994
        """
        