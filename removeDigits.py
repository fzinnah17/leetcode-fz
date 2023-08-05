"""
You are given an integer n. On each step, you may subtract one of the digits from the number.

How many steps are required to make the number equal to 0?

State/Subproblem: For an integer i, number of steps to make it to 0
Transition/Formula: dp[i] = i - remainder(i if i ! = 0, but if if remainder i == 0, then i - quotient)
base case: if digit < 10: i - i subtract itself to return 0
final subproblem: dp[n]
"""
