class Solution(object):
    def insert(self, intervals, newInterval):
        """
    Pseudocode:
    1. Append the new interval to the intervals array: intervals.append(newInterval)
    2. Sort the intervals array based on the start value: intervals.sort(key=lambda x: x[0])
    3. Initialize an empty stack: stack = []
    4. Push the first interval from the sorted intervals array onto the stack: stack.append(intervals[0])
    5. Iterate through the remaining intervals using a for loop (starting from index 1):
        a. Retrieve the current interval's start value: curr_start = intervals[i][0]
        b. Retrieve the previous interval's end value from the top of the stack: prev_end = stack[-1][1]
        c. Compare curr_start with prev_end:
            i. If curr_start is less than or equal to prev_end, merge the intervals by updating the end value of the top interval in the stack: stack[-1][1] = max(stack[-1][1], intervals[i][1])
            ii. Otherwise, push the current interval onto the stack: stack.append(intervals[i])
    6. Create an output array:
        a. Iterate through the intervals in the stack:
            i. Append each interval to the output array: output.append(stack[i])
    7. Return the output array
        """
        intervals.append(newInterval)
        intervals.sort(key = lambda x : x[0])
        stack = []
        stack.append(intervals[0])
        for i in range(1,len(intervals)):
            currStart = intervals[i][0]
            prevEnd = stack[-1][1]
            if currStart <= prevEnd:
                stack[-1][1] = max(stack[-1][1],intervals[i][1])
            else:
                stack.append(intervals[i])
        output = []
        for i in stack:
            output.append(i)
        return output
                
        
        
        
        