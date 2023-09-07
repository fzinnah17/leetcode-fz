"""
Given a string s, return true if a permutation of the string could form a palindrome and false otherwise.

Example 1: Input: s = "code" Output: false

Example 2: Input: s = "aab" Output: true

Example 3: Input: s = "carerac" Output: true
 
Constraints: 1 <= s.length <= 5000, s consists of only lowercase English letters.
"""
def canPermutePalindrome(s):
  count = 0
  charCounter = Counter(s)
  for ch in charCounter:
      #odd
      if charCounter[ch] % 2 != 0:
          count += 1
          if count > 1:
              return False
  return True
"""
Pseudocode:
1. variable count to keep track of how many characters in the string occur an odd number of times. 
2. counter to keep track of how many times the characters appeared regardless of being odd/even
3. iterate through the counter character by character:
        print(charCounter[ch]) -> 2
                                  2
                                  2
                                  1
        print(charCounter) ->     Counter({'c': 2, 'a': 2, 'r': 2, 'e': 1})
    a. For odd/central character:
            i. if the character count is not divisible by 2:
                    the odd number of occurrence can go up by 1
                    If we find more than one character with an odd frequency, return False, as the string cannot be rearranged to form a palindrome without the central character.
4. return true if the loop completes without returning False, it means the string can be rearranged to form a palindrome

TC: O(n)
SC: O(k) k is the unique number of characters

Here we're trying to figure out if a string can be rearranged to form a palindrome. That's why, we are using a frequency counter to help determine the number of odd frequencies in the string. The string can be a palindrome if it has at most one central character that occurs an odd number of times.

If count is less than or equal to 1, then the string can be rearranged to form a palindrome. The time complexity with this approach is O(n) due to the single pass through the string and the space complexity is O(k), where k is the number of unique characters in s.

"""
