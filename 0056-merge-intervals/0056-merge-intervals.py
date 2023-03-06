class Solution(object):
    def merge(self, intervals):
        """
        TC: O(nlogn) because we are sorting
        SC: O(N) for using priority queue
        """
        intervals.sort()
        prQueue = []
        prQueue.append(intervals[0])

        for i in range(1,len(intervals)):
            curr = intervals[i]
            prev = prQueue[-1]
            if curr[0] <= prev[1]:
                prQueue[-1][1] = max(curr[1],prev[1])
            else:
                prQueue.append(curr)
        return prQueue
                
            
        