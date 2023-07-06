class Solution(object):
    def merge(self, intervals):
        """
        Pseudocode:
        Edge case: the intervals length <= 1 means just return the intervals array itself.
        1. sort the array based on the start values
        2. variables: output = [] we will compare the the first array as it doesn't have any previous so adding it in the output list initially.
        3. traverse the array from the 1st index to the length:
            a. current array start value < previous array end value:
                    merge those by taking the max value
            b. else: current array start value > previous array end value:
                    append that array in the output array
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