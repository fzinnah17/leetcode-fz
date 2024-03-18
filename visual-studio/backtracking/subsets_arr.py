"""
Problem: Given an integer array nums of unique elements, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

The aim is to return a list with all the subsets without any duplicates.

Keyword arguments:
argument -- nums: an array of integers
Return: a list of lists with all the subsets with no duplicate subset
"""

def subsets(nums):
    res = []
    curr = []

    def dfs(i):
        if i >= len(nums):
            res.append(curr[:])
            return
        
        #include the number
        curr.append(nums[i])
        dfs(i + 1)

        #do not include the number
        curr.pop()
        dfs(i + 1)
    dfs(0)
    return res
if __name__ == '__main__':
    testcases = [
        [1,2,3],
        [2],
        [2,3],
        []
    ]

for i, nums in enumerate(testcases):
    result = subsets(nums)
    print(f"Test case {i} returns the following subsets: {result}")