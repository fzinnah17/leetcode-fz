"""

Problem: Given an array of strings nums containing n unique binary strings each of length n, return a binary string of length n that does not appear in nums. 
         If there are multiple answers, you may return any of them.

        - Function returns a unique string that is not present in the input list.
        - arguments/inputs: nums array that contains binary strings of length n
        - Returns: It returns a unique binary string that is not present in the input list. If the input list is empty, it returns an empty string.
Plan:
     input: ["1001", "0110", "1100", "0000"] 4 unique binary strings each should be length of 4
    output: different binary string than the inputs. Should I return the output string inside a list or as a string? 'return a binary string'**
"""


def unique_binarystring(nums):
    res = ""
    curr_str = []
    # Set for faster lookup to check if a binary string is unique
    num_set = set(nums)

    if len(nums) == 0:
        return " "

    def dfs(i):
        """
        - Function: perform depth first search to build a unique string that is not present in the input list
        - Argument: i is the index that is the current position of the binary string that is being built now
        """

        # nonlocal is used so that we do not create a local variable res and use the global variable to return the result
        nonlocal res

        # Stop if a result is already found

        if res:
            return

        if i >= len(nums[0]):
            # we are using join method because we are returning a string as an output, otherwise we ould use [:] instead if we had to return a list
            candidate = "".join(curr_str)
            # we are checking the set because it can help to ensure the result we are returning does not already exist in the array according to the problem constraint
            if candidate not in num_set:
                res = candidate
                return
        if res:
            return

        # Continue only if we haven't reached the target length
        if i < len(nums[0]):
            # add "0" to explore the possibility with "0" at the current position
            curr_str.append("0")
            # we are using backtracking to explore other strings that is not present in the input array
            dfs(i + 1)
            curr_str.pop()

            # Check if the result was found before proceeding to the next branch
            if res:
                return res

            # add "1" to explore the possibility with "1" at the current position

            curr_str.append("1")
            # we are using backtracking to explore other strings that is not present in the input array
            dfs(i + 1)
            curr_str.pop()

    dfs(0)
    return res


if __name__ == "__main__":
    # Each testcase is checking for the input strings and calling the backtracking helper function to find another string of the same length
    testcases = [
        [""],
        ["1"],
        ["10", "01"],
        ["111", "011", "001"],
        ["1001", "0110", "1100", "0000"],
    ]

for i, nums in enumerate(testcases):
    res = unique_binarystring(nums)
    print(f"Testcase {i + 1} result is {res}")
