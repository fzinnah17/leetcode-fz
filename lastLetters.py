"""
Make a new string from the last two letters of a string, but with the letters switched around and a space between them.
Example
Return 't a' when the word 'bat' is given.
Description of What It Does
Fill out the function lastLetters in the editor below.
Here are the parameters for lastLetters:
string word: a group of characters that will be processed
Returns a string: A pair of characters with spaces between them
"""
def lastLetters(word):
    """
    Pseudocode:
    1. variable = empty string
    2. reverse the current string
    3. use a slice operator to extract the first two letters of the reversed string
    4. join the characters using a space in between"""
    
    word = word[::-1] #.reverse() can't be used here as it can be only used in the list
    word = word[:2]
    spacedWord = ' '.join(word)
    return spacedWord
