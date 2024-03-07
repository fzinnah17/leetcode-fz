"""
Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

summary_line: Determining a function that partitions the string in a way to make those palindromes

Keyword arguments:

s -- string to be partitioned into palindromes

Return: returning a list of strings that are palinfromes of the given string

testcases -> s = "aab" return ["aa", "b"]
            s = "a" return ["a"]
            s = "aabb" return ["aa", "bb"]
            s = "abba" return ["a", "b", "b", "a"]

plan:

"""

def partition(s):
   if len(s) == 1:
       return s[0]


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
        print(f"Testcase {i + 1} returns {res}")