class Solution(object):
    def minMeetingRooms(self, intervals):
        # intervals = sorted(intervals, key = lambda x: x[0]) trying???
        #this prints [[10, 15], [15, 16], [16, 25]] based on the start value
        intervalStart, intervalEnd = [], []
        for i in range(len(intervals)):
            intervalStart.append(intervals[i][0])
            intervalEnd.append(intervals[i][1])
        intervalStart.sort()
        intervalEnd.sort()
        print (intervalStart, intervalEnd)
        #this prints (([3, 5, 9, 12]
        #                  t
        #              [5, 6, 14, 19]) -> [3,6], [9,19]
        #               b
        
        topPointer, bottomPointer = 0,0 #I will have two pointers top and bottom
        roomNeeded, count = 0,0
        while topPointer < len(intervalStart):
            if intervalStart[topPointer] < intervalEnd[bottomPointer]:
                topPointer += 1 #if top pointer > bottom pointer, then room Needed += 1
                count += 1
            # elif intervalStart[topPointer] == intervalEnd[bottomPointer]:
            #     bottomPointer += 1                      
            else:
                bottomPointer += 1
                count -= 1 ## but we will have count just in case if a meeting is finished
            roomNeeded = max(roomNeeded, count)
        return roomNeeded

                
        
        
        