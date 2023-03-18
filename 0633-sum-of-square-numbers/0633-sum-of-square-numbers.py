class Solution(object):
    def judgeSquareSum(self, c):
        """
        Pseudo code:
        1. left = 0
        2. right = sqrt(c)
        3. while loop:
            sum = left^2 + right^2
            if sum <c: l += 1
            if sum > c : r -= 1
            if sum == c:
            return True
        return false
        TC: O(sqrt(c))
        SC: O(1)"""
        left = 0
        right = int(sqrt(c))
        while left <= right:
            currSum = (left ** 2) + (right ** 2)
            if currSum < c:
                left += 1
            if currSum > c:
                right -= 1
            if currSum == c:
                return True
        return False


# """When discussing the time complexity of an algorithm, we are essentially trying to quantify how the running time of the algorithm scales with the size of the input. In this case, the input is a non-negative integer c. First, lets consider the brute force approach. This involves checking every possible pair of integers (a, b) to see if a^2 + b^2 = c. Since we need to check pairs of integers up to sqrt(c), the time complexity of this approach would be O(sqrt(c)^2), which simplifies to O(c). This means that as the input value c grows larger, the running time of the algorithm will grow linearly with c. On the other hand, the two pointers approach involves using two pointers (one starting at 0 and one starting at sqrt(c)) to traverse the possible pairs of integers more efficiently. In this case, the running time of the algorithm scales with the square root of the input value, because we only need to traverse pairs of integers up to sqrt(c). This means that the time complexity of the two pointers approach is O(sqrt(c)). As the input value c grows larger, the running time of the algorithm will grow at most proportionally to the square root of c. To summarize, the brute force approach has a time complexity of O(c), which means that it will become increasingly slow as the input value c grows larger. The two pointers approach has a time complexity of O(sqrt(c)), which means that it will be much more efficient for larger input values.
#  """    
        