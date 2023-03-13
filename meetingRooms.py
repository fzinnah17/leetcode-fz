def canAttendMeetings(self, intervals):
        """
        Pseudocode:
        1. sort the intervals based on start time
        2. lst to add the first element
        3. traverse through the input list
            a. compare current and previous(adjecent):
                i. if curr[0] < prev[1]:
                    return False
                ii. add into the current list
            return True
        TC: O(nlogn) SC: O(n)
        """
    if len(intervals) < 2:
          return True
    intervals.sort()
    lst = []
    lst.append(intervals[0])

    for i in range(1, len(intervals)):
        prev = lst[-1]
        curr = intervals[i]
        if curr[0] < prev[1]:
            return False
        lst.append(curr)
    return True
