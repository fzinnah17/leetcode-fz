class Solution:
    def maxLength(self, arr: List[str]) -> int:
        max_len = 0
        combination = []

        def dfs(index):
            nonlocal max_len
            if index >= len(arr):
                if len(set(''.join(combination))) == len(''.join(combination)):
                    max_len = max(max_len, len(''.join(combination)))
                return

            # Include the current string in the combination
            combination.append(arr[index])
            dfs(index + 1)

            # Exclude the current string from the combination
            combination.pop()
            dfs(index + 1)

        dfs(0)
        return max_len
