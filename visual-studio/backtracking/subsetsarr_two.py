"""

Problem: Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

The aim is to create a subsets list that is created from the input list which has duplicates in it.

Keyword arguments:
argument -- nums: an array of integers that is also duplicated
Return: a list of list that contains the subsets without any duplicates
"""

def subsetswithDuplicates(nums):
    res = set() #to not have any duplicates in the returned subset list
    curr = []
    nums.sort()

    def dfs(i):
        print(f"Current set is: {curr}")
        if i >= len(nums):
            res.add(tuple(curr[:]))
            return

        curr.append(nums[i])
        dfs(i + 1)
        print(f"Current set is: {curr}")

        curr.pop()
        dfs(i + 1)

        print(f"Current set is: {curr}")


    dfs(0)
    return res

if __name__ == "__main__":
    testcases = [
        [2,3,2],
        [1],
        [],
        [4,9,9,10,10,11,12,13,13]
    ]

for i, nums in enumerate(testcases):
    result = subsetswithDuplicates(nums)
    print(f"Testcase {i} can create this subset: {result}")
