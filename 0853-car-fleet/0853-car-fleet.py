class Solution(object):
    from collections import deque
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        https://leetcode.com/problems/car-fleet/discuss/1335749/Python-3-Visual-Examples
        """
        #1. In a list, add the position and the speed:
        carVals = []
        for i in range(len(position)):
            carVals.append([position[i],speed[i]])
        #2. Sort the list from right to left according to the position because we need to reach a target mile which is in reverse bc usually we go left to right
        carVals.sort(reverse = True) #[[10, 2], [8, 4], [5, 1], [3, 3], [0, 1]]
        stack = []
        #3. iterate through the list:
        for pos, speed in carVals:
            #4. Calculate and record time for each car to reach destination in the stack:
            time = float(float((target - pos)) / float(speed))
            stack.append(time)
            # #5. Because I am adding right to left and right is going to my stack's bottom and left is coming on top of the stack
            # """rightCarbottom = stack[-2]
            # leftCartop = stack[-1]"""
            # #6. Check if the fleets overlap. If so, pop it out
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                #7. Remove the top aka lowest time
                stack.pop()
        #8. Return the cars that never overlapped
        return len(stack)
        
            
            
        