"""Question:
Given an array of strings wordsDict and two different strings that already exist in the array word1 and word2, return the shortest distance between these two words in the list.

Example 1:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "coding", word2 = "practice"
Output: 3
Example 2:

Input: wordsDict = ["practice", "makes", "perfect", "coding", "makes"], word1 = "makes", word2 = "coding"
Output: 1

Constraints:

2 <= wordsDict.length <= 3 * 104
1 <= wordsDict[i].length <= 10
wordsDict[i] consists of lowercase English letters.
word1 and word2 are in wordsDict.
word1 != word2"""


class Solution(object):
    def shortestDistance(self, wordsDict, word1, word2):
        """
        PSEUDOCODE:
        
        Check if word1 and word2 are the same before performing any distance calculations. If they are the same, return 0.
        
        1. To implement the approach of storing indices in a dictionary to subtract later during our calculation, we can use the built-in defaultdict class that provides a default value for a nonexistent key, which makes it useful for this purpose.
        2. output = float(inf), a variable to store the shortest distance. Initialize it to a large value initially, and update it whenever you find a shorter distance.
        3. Using a for loop start iterating the list:
            a. if condition: check if word1 in the list
                b. Use another for loop to check for word2:
                    if condition: check if word2 in the list:
                        distance = abs(index[word1] - index[word2])
                        output = min(distance, output)
            SO WHAT IF I HAVE ANOTHER SHORTEST DISTANCE? HOW WOULD I KEEP TRACK OF IT? USING THE 'min' function
        4. Return output
        """
        word_indices = defaultdict(list)
        output = float("inf")
        if word1 == word2:
            return 0
        for i in range(len(wordsDict)):
            if wordsDict[i] == word1:
                for j in range(len(wordsDict)):
                    if wordsDict[j] == word2:
                        distance = abs(i - j)
                        output = min(output, distance)               
        return output
    """TC: O(n^2) for using nested loops
       SC: O(n) defaultdict is used to store the indices of the words. In the worst case, where each word is unique, the defaultdict will store n entries, where n is the number of words in wordsDict"""

    
        
