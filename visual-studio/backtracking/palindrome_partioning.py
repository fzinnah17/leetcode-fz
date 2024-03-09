"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

summary_line: Determining a function that partitions the string in a way to make those palindromes

Keyword arguments:

s -- string to be partitioned into palindromes

Return: returning a list of strings that are palindromes of the given string

testcases -> s = "aab" return ["aa", "b"]
            s = "a" return ["a"]
            s = "aabb" return ["aa", "bb"]
            s = "abba" return ["a", "b", "b", "a"]

plan:
    iterate over the string from i to length of the string
    if the i an j the same aka palindrome helper function, then return true
    else return false

    for the helper function,
        if the characters from both end are the same then return true
"""

def partition(s):
    res = []
    parts = []

    def is_palindrome(s, l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True   

    def dfs(i):
        if i >= len(s):
            res.append(parts[:])
            return
        
        for j in range(i, len(s)):
            if is_palindrome(s, i, j):
                parts.append(s[i : j + 1])
                dfs(j + 1)
                parts.pop()
    dfs(0)
    return res

if __name__ == "__main__":
    #These testcases should partition in a way to return the palindrome strings

    testcases= [
        "aab",
        "a",
        "b",
        "aabb",
        "abba",
        "aabbcc"
    ]

    #I should have the inputs with the "i"
    for i, s in enumerate(testcases):
        res = partition(s)
        print(f"Testcase {i + 1} : {testcases[i]} returns {res}")