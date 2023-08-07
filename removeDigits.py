"""
You are given an integer n. On each step, you may subtract one of the digits from the number.

How many steps are required to make the number equal to 0?


Greedy:
I am greedily choosing the largest digit to subtract, aiming to minimize the number of steps

State/Subproblem: dp[i] = minimum number of steps to reach 0 from ith/num value
Transition/formula: Taking the Maximum digit of the given number and subtracting it. 
                    So, n = n - max(n % 10, recursion(quotient of that n))
Base case: if n == 0: return 0
Final subproblem:dp[n]

TC: O(n×m), where n is the value of the number and m is the number of digits in n. This is because, in the worst case, 
    for each subtraction operation (which can be at most n times), you might be finding the maximum digit (which can take up to 
    m operations). The largest digit might be the 1st digit of that number which will require to traverse from end to start passing all the m digits.
SC: O(m) due to the recursive stack space, where m is the number of digits.

n = 5 => Steps = 1 (Just subtract 5)
n = 11 => Steps = 2 (Subtract 1, then 1 again)
n = 123 => Steps = 3 (Subtract 3, then 2, then 1)
n = 202 => Steps = 2 (Subtract 2, then 2 again)
n = 987654 => Steps = 6 (Subtract 9, then 8, then 7, then 6, then 5, then 4)
"""

def removeDigits(n):
  def extractMaxDigit(num):
    if num == 0:
      return 0
    else:
      modulo = num % 10
      quotient = num // 10
      return max(modulo, extractMaxDigit(quotient))
  
  steps = 0
  while n > 0:
      maxDigit = extractMaxDigit(n)
      n = n - maxDigit
      steps += 1
  return steps

"""
Recursive Approach using Dynamic Programming:

1. **State/Subproblem**:
    - dp[i] = minimum number of steps required to reduce the number i to 0 by subtracting one of its digits at each step.
  
2. **Transition/Formula**:
    - For every digit d of the current number i, consider i - d. 
    - dp[i] = min(dp[i - d] + 1). The +1 here represents the step I have to take to subtract the digit.
  
3. **Base Case**:
    - dp[0] = 0, because if the number is already 0, you don't need any steps.
  
4. **Final Subproblem**:
    - dp[n] = the minimum number of steps required to reduce n to 0.

### Example:

Let's say n = 213.

- For i = 1, the only digit is 1. So, dp[1] = 1 + dp[1-1] = 1 + dp[0] = 1 + 0 = 1.
- For i = 2, the only digit is 2. So, dp[2] = 1 + dp[2-2] = 1 + dp[0] = 1 + 0 = 1.
- For i = 3, the only digit is 3. So, dp[3] = 1 + dp[3-3] = 1 + dp[0] = 1 + 0 = 1.
- For i = 213, the digits are 1, 2, and 3. 
  - dp[213] = min(1 + dp[213-1], 1 + dp[213-2], 1 + dp[213-3]).

We calculate for all numbers from 1 to 213 and use the memoized results to get our final solution for dp[213].

### TC:

- The calculation for each number i involves iterating over its digits. In the worst case, a number i can have log_{10}(i) digits.
- The maximum number we go up to is n. Thus, our TC is O(nlog_{10}(n)).

### SC:

- We need an array [memoTable] to store our results for each number from 0 to n. Thus, the space complexity is O(n).
- If considering the recursion stack (for very large numbers), the space complexity can go up due to deep recursion (the depth being equivalent to the number of digits). However, in most scenarios, this depth isn't a concern.

In this code:

We use a memoization table (memo) to store already computed solutions.
We define a recursive function dp that computes the minimum steps required to reduce a number to 0. It considers each digit of the number, computes the number of steps if that digit is subtracted, and takes the minimum.
We call this dp function on the input number n and return the result.

def removeDigits(n):
    # Initialize memoization table with -1 (indicating not computed yet)
    memo = [-1 for _ in range(n+1)]
    
    # Base Case
    memo[0] = 0

    def dp(num):
        # If the value is already computed, return it
        if memo[num] != -1:
            return memo[num]
        
        # Get the individual digits of the number
        digits = [int(d) for d in str(num)]
        
        # Compute the number of steps required for each digit subtraction
        # and take the minimum
        min_steps = float('inf')  # Initialized with a large value
        for d in digits:
            min_steps = min(min_steps, 1 + dp(num - d))
        
        # Store the computed value in the memo table
        memo[num] = min_steps

        return min_steps

    return dp(n)

# Test
n = 213
print(removeDigits(n))  # Expected output: 3


### Takeaway:

This problem showcases the flexibility in problem-solving. While it can be tackled with a greedy approach (subtracting the largest digit), it can also be seen from a dynamic programming viewpoint by breaking down the problem into smaller chunks and building the solution from those smaller chunks. 

When attempting other problems in the future, always consider:

1. What's the main problem I am trying to solve?
2. Can I break that problem into smaller subproblems?
3. Do solutions to smaller subproblems help in solving the bigger problem?
4. Are there overlapping subproblems? If yes, then memoization or tabulation will help.

By addressing these questions, I can decide whether a DP approach is suitable or if another method, like greedy algorithms, would be more appropriate.
"""
