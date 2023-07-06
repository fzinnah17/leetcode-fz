class Solution(object):
    def merge(self, intervals):
        """
        Pseudocode:
        Edge case: the intervals length <= 2 means just return the intervals itself.
        1. sort the array based on the start values
        2. variables
        3. traverse the array:
            a. current array start value > previous array end value:
                    merge those
            b. else: current array start value < previous array end value:
                    append those in the output array
        TC: O(nlogn) SC: O(n)
        """
        if len(intervals) <= 1:
            return intervals
        intervals.sort(key = lambda x : x[0]) #sort based on the starting value
        output = []
        output = [intervals[0]]
        for i in range(1,len(intervals)):
            if intervals[i][0] <= output[-1][1]:
                output[-1][1] = max(intervals[i][1],output[-1][1])
            else:
                output.append(intervals[i])
        return output
