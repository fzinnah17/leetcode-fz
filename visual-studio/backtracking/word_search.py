""""
Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. 
The same letter cell may not be used more than once.
"""

def matchWord(board, word):
    """Determines if the word exists in the grid following specific rules.

    Args:
        board: A list of lists of characters representing the grid.
        word: A string representing the word to be matched in the grid.

    Returns:
        A boolean value indicating whether the word exists in the grid.

    Raises:
        Specific exceptions that you expect your function to throw, e.g., ValueError if there are input validation checks (not applicable here).

    plan:
        1. If the word[0] is matching with the current character then I will call the helper function

    Time Complexity: O(N), where N is the number of cells in the grid. in the worst-case scenario, we might need to traverse all the cells in the grid to find the desired word.
    Space Complexity: O(N), for using visited set.
     [
                ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
            ],
            "FCSEDA",
            False
    """

    visited = set()

    def dfs(row, col, pointer):
        if len(word) == pointer:
            return True
        
        if row < 0  or col < 0 or row >= len(board) or col >= len(board[0]) or (row, col) in visited or board[row][col] != word[pointer]:
            return False
        
        visited.add((row, col))
        
        res = (
            dfs(row + 1, col, pointer + 1) or
            dfs(row - 1, col, pointer + 1) or
            dfs(row, col + 1, pointer + 1) or
            dfs(row, col - 1, pointer + 1)
        )

        visited.remove((row,col)) #always write why we did it? -> Backtrack to explore other potential paths.
        return res

    for r in range(len(board)):
        for c in range(len(board[0])):
            if board[r][c] == word[0]:
                if dfs(r,c,0):
                    return True
    return False

if __name__ == "__main__":
    # Both test cases: Check if the function correctly identifies an existing word in the grid.

    testcases = (
        (
            [
                ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
            ],

            "ABCESE",
            True
        ),
        (
            [
                ["A","B","C","E"],
                ["S","F","C","S"],
                ["A","D","E","E"]
            ],
            "FCSEDA",
            False
        )
    )

for i, (board, word, expected) in enumerate(testcases):
    res = matchWord(board, word)
    print(f"Testcase {i + 1} is {res == expected}")
    if res != expected:
        print(f"Test case {i + 1} failed: expected {expected}, got {res}")