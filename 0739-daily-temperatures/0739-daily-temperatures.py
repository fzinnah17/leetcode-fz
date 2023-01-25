class Solution(object):
    from collections import deque
    def dailyTemperatures(self, temperatures):
        w = len(temperatures)
        result, stack = [0]*w, deque()
        for i in range(w):
            while stack and temperatures[stack[-1]] < temperatures[i]:
                index = stack.pop()
                result[index] = i-index
            stack.append(i)
        return result
        """
        :type temperatures: List[int]
        :rtype: List[int]
        In this problem, we are given a list of temperatures, where the temperature at index I is the temperature for the ith day. Our goal is to calculate how many days it will take until the next day is warmer than the current day for each day. When attempting to solve a problem, a brute-force approach is frequently the best place to start. The simplest or brute-force solution is to go through the array and, for each day, go through all the other days until you find one with a higher temperature. Because N105 constraints are in place, this method would take O(N2) time, which is extremely slow. What's the issue about using brute force?
        I built a nested loop. I iterate through each element in the outer loop, and in the inner loop, I search the remainder of the list for the next greater value to the current element.

The issue here is that this brute force algorithm has a lot of redundant operations that need to be eliminated, so we should try only to visit each element once.
https://liuzhenglaichn.gitbook.io/algorithm/monotonic-stack
The [0] * x creates a list with x elements. So,

>>> [ 0 ] * 5
[0, 0, 0, 0, 0]
        """
            
        