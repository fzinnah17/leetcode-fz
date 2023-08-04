"""
Your task is to count the number of ways to construct sum n by throwing a dice one or more times. Each throw produces an outcome between 1 and 6.
For example, if n = 3, there are 4 ways:
• 1+1+1
• 1+2
• 2+1
• 3

Input: N = 2
Output: 2
Explanation:
The two possible ways to obtain N are:

1 + 1
2

State/Subproblem: dp[i]-> the number of ways to construct the i sum (i = curr position/value)
Transition/Formula: dp[i] = Σ dp[i-k] 
                        k = 0 to k = 6 [6 possibilities we have as we throw our dice to make the given sum n]
                    dp[i] = dp[i-1] + dp[i-2] + dp[i-3] + dp[i-4] + dp[i-5] + dp[i-6]


Pseudocode:
1. Create a function called numberofWays that takes an input n.
2. Initialize a list called memoTable with -1 repeated n + 1 times to create an array with the placeholder -1.
3. Define a helper function called numberOfWaysHelper that takes an input n.
      Inside the numberOfWaysHelper function:
            a. If n is less than 0, return 0 (because we cannot have negative ways).
            b. If n is 0, return 1 (as there's only one way when we don't make any moves).
            c. If the value of memoTable at index n is not equal to -1, return the value from memoTable at index n. This is done to avoid redundant calculations and store previously computed results.
            d. Set the value of memoTable at index n to 0 (as we will calculate the number of ways for this value).
            e. Use a loop to iterate from 1 to 6 (inclusive):
                     i. Call the numberOfWaysHelper function recursively with n - i as the input and add the result to the value at index n in memoTable.
                    ii. Return the value at index n in memoTable, which now holds the total number of ways to reach the target n.
4. Return the result of calling the numberOfWaysHelper function with the input n as the argument. This gives us the total number of ways to reach n using the given rules.

TC: O(n) because the function uses memoization (dynamic programming) to store previously computed results in the memoTable. 
    It calculates the number of ways for each value of n only once and then reuses the stored results when needed, avoiding redundant calculations.
sc: O(n) because the memoTable list is created with a size of n + 1, and it stores the computed results for each value of n. 
    The recursion depth for the numberOfWaysHelper function also contributes to the space complexity, 
    but since the recursion is limited to a maximum of n, it does not exceed the space used by the memoTable.
"""

def numberofWays(n):
    memotTable = [-1] * (n + 1)

    def numberOfWaysHelper(n):
        if n < 0:
            return 0
        if n == 0:
            return 1
        if memotTable[n] != -1:
            return memotTable[n]
        memotTable[n] = 0
        for i in range(1, 7):
            memotTable[n] += numberOfWaysHelper(n - i)
        return memotTable[n]

    return numberOfWaysHelper(n)
