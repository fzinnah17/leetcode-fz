class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        minWordLen = 11
        for word in wordDict:
            minWordLen = min(len(word), minWordLen)
            
        def dfs (remainder):
            res = []
            if len (remainder) == minWordLen and remainder in wordDict:
                return [remainder]
            elif len(remainder) < minWordLen:
                return []
            else:
                for i in range(len(remainder)):
                    word = remainder[:i + 1]
                    if word in wordDict:
                        if remainder[i+1:] == "":
                            res.append(word)
                        else:
                            sentences = dfs (remainder[i+1:])
                            for sentence in sentences:
                                res.append (word + " " + sentence)
            return res
        return dfs(s)
        