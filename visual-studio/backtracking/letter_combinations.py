"""
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.
Note that 1 does not map to any letters."""

"""sumary_line: A function that returns all possible letter combinations from the input number

Keyword arguments: s: A string that has digits from 2-9

Return: returning a list that has all the letter combinations from that given number

plan:
    1. empty string
    2. string length 1
    3. create a dictionary with key as number and value as letters
    4. write the helper function
    5. iterate over the string and call the helper function
        a. iterate over the map to do the backtracking

        Time complexity: O(4^n)
        Space complexity: O(n)
"""


def letter_combinations(s):
    # key = number and value = letters
    num_map = {
        "2": "abc",
        "3": "def",
        "4": "ghi",
        "5": "jkl",
        "6": "mno",
        "7": "pqrs",
        "8": "tuv",
        "9": "wxyz",
    }
    if not s:
        return []
    if len(s) == 1:
        return list(num_map[s])

    res = []
    combs = []

    def dfs(i):
        if i >= len(s):
            res.append("".join(combs))
            return

        for char in num_map[s[i]]:
            combs.append(char)
            dfs(i + 1)
            combs.pop()

    dfs(0)
    return res


if __name__ == "__main__":
    testcases = ["23", "7", "45", "89"]

for i, s in enumerate(testcases):
    res = letter_combinations(s)
    print(f"Testcase {i + 1}: {s} returns {res}")
