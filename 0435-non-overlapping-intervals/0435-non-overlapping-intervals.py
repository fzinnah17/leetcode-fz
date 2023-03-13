class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        Pseudocode:
        1. Sort the list based on start time
        2. Edge case: intervals length = 1 means just return output = 0
        3. create a list
        4. insert the first element in the list
        5. traverse the input
            a. check if the current' start time > previous' end time
                    i. If so, then add it in the list
        6. return the len(intervals) - len(nonoverLapping)
        TC: O(NLOGN) SC: O(N)
        """
        output = 0
        if len(intervals) == 1:
            return output
        intervals.sort() #[[1,2],[1,3],[2,3],[3,4]]
        nonoverLapping = []
        nonoverLapping.append(intervals[0])
        
        for i in range(1,len(intervals)):
            prev = nonoverLapping[-1]
            curr = intervals[i]
            if curr[0] >= prev[1]: #nonoverlapping
                prev[1] = curr[1]
            else: #overlapping
                output += 1
                prev[1] = min(curr[1],prev[1])
        return output
                
        