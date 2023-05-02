class Solution(object):
    def mySqrt(self, x):
        """   
When you encounter a problem like this, the first step is to think about the time and space complexities of the different possible solutions. In this case, a brute force solution would be to iterate through all numbers from 0 to x and check which one squared is closest to x. However, this solution has a time complexity of O(x) and is not efficient for large x.

Next, you can think about other algorithms that might be more efficient. In this case, binary search is a good candidate because the square root of a number x is always between 0 and x. You can use binary search to find the number n such that n^2 <= x < (n+1)^2. Once you have found n, you can return it as the square root of x.

Using binary search has a time complexity of O(log x), which is much better than the brute force solution. Therefore, when you encounter a problem that involves finding a value within a range, binary search is often a good algorithm to consider.
        """
        if x == 0:
            return 0
        if x == 1:
            return 1
        left, right = 2, x
        while left <= right:
            middle = left + ((right - left) // 2)
            if middle * middle == x: # 2 = sqrt(4) => 2^2 = 4
                return middle
            elif middle * middle > x: # 5 > sqrt(4) => 5^2 = 4
                right = middle - 1
            else:
                left = middle + 1 # 1 < sqrt(4) => 1^2 = 4
        return right
    #TC: O(n) SC: O(1)
            