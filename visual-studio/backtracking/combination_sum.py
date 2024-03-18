"""

Problem: Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

The test cases are generated such that the number of unique combinations that sum up to target is less than 150 combinations for the given input.

Keyword arguments:
argument -- nums: array of unique integers
         -- taget: an integer to compare the sum of the combinations
Return: A list of lists that has all the unique combinations of the array that sums up to target
"""

def combinationSum(nums, target):
    res = []
    candidates = []
    # curr_sum = 0

    def dfs(i,curr_sum):
        # nonlocal curr_sum
        # print(f"Entering dfs with i = {i}, curr_sum = {curr_sum}")


        if curr_sum == target:
            res.append(candidates[:])
            return
        if curr_sum > target or i >= len(nums):
            return
        
        for j in range(i, len(nums)):
            #to include
            candidates.append(nums[j])
            dfs(j, curr_sum + nums[j])

            #to not include
            candidates.pop()
            dfs(j + 1, curr_sum)
    dfs(0, 0)
    return res

if __name__ == '__main__':
    testcases = [
        ([], 1),
        ([1],2),
        ([3],3),
        ([1,3,7,9], 10),
        ([2,3,6,7], 7)
    ]

for i, (nums, target) in enumerate(testcases):
    result = combinationSum(nums, target)
    print(f"Testcase {i}: {testcases[i]} has the following combination {result} returning the {target}")