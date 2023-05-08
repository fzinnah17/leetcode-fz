class Solution(object):
    def reverseVowels(self, s):
        """
        Pseudocode:
        1. Create own SET of vowels to check if the string characters are vowel or not
        2. Have two pointers
            a. P1 to start in the beginning
            b. P2 to start from the end
        3. iterate through the string using while loop until the two pointers meet in the middle of the string
        4. As iterating,
            we will check:
                if P1 = vowel and P2 = vowel, then we can swap those, but in Python strings are immutable/unchangeble/fixed/cant be changed, meaning that you cannot change a string in-place. Thus, the swapping s[left],s[right] = s[right],s[left] will not work.
                if P1 = vowel and P2 != vowel, then we can increment P1 and decrememnt P2 till P2 cross P1
        5. At the end we can return the string
        """
        vowels = ["a","e","i","o","u","A","E","I","O","U"]
        lst = list(s)
        left = 0
        right = len(s)-1
        while left <= right:
            if lst[left] in vowels and lst[right] in vowels:
                lst[left],lst[right] = lst[right],lst[left]
                left += 1
                right -= 1
            elif lst[left] in vowels:
                right -= 1
            else:
                left += 1
        output = "".join(lst)
        return output
            
        