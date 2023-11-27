class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        # Initialize the minimum word length to a large value (11 in this case)
        minWordLen = 11
        for word in wordDict:         # Iterate through each word in the word dictionary
            minWordLen = min(len(word), minWordLen)  # Update minWordLen to be the minimum of the current word length and the current minWordLen
        # Define a depth-first search (DFS) function to explore all possible word break combinations
        def dfs(remainder):
            res = []  # Initialize an empty list to store the result
            # Check if the remaining string has a length equal to minWordLen and is in the word dictionary
            if len(remainder) == minWordLen and remainder in wordDict:
                return [remainder]  # If so, return a list containing the remaining string
            # Check if the remaining string is shorter than minWordLen
            elif len(remainder) < minWordLen:
                return []  # If so, return an empty list since no valid word break is possible
            # If the remaining string is longer than or equal to minWordLen
            else:
                for i in range(len(remainder)): # Iterate through each index in the remaining string
                    word = remainder[:i + 1]  # Extract a substring from the beginning up to the current index
                    if word in wordDict:  # Check if the extracted word is in the word dictionary
                        if remainder[i+1:] == "":  # If the rest of the string is empty
                            res.append(word)  # Add the current word to the result list
                        else:
                            sentences = dfs(remainder[i+1:])  # Recursively call the DFS function on the remaining substring
                            for sentence in sentences:  # Concatenate the current word with each sentence obtained from the recursive call
                                res.append(word + " " + sentence)
            return res  # Return the final list of word break combinations
        return dfs(s)   # Call the DFS function with the input string 's'