class Solution(object):
    def insert(self, intervals, newInterval):
        """
The time complexity of your implementation is O(nlogn) because of the sorting step. The space complexity is also O(n) because the priority queue (implemented using a list) can contain up to n elements in the worst case.
        """
        intervals.append(newInterval)
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
        