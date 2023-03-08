class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        """
        i, j = 0, 0
        result = []
        while i < len(firstList) and j < len(secondList):
            start = max(firstList[i][0], secondList[j][0])
            end = min(firstList[i][1], secondList[j][1])
            if start <= end:
                result.append([start, end])
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1
        return result





        # firstList.extend(secondList) #[[0, 2], [5, 10], [13, 23], [24, 25], [[1, 5], [8, 12], [15, 24], [25, 26]]]
#         mergedLists = firstList + secondList
#         mergedLists.sort() #[[0, 2], [1, 5], [5, 10], [8, 12], [13, 23], [15, 24], [24, 25], [25, 26]]

#         prQueue = []
#         prQueue.append(mergedLists[0])
#         for i in range(1,len(mergedLists)):
#             curr = mergedLists[i]
#             prev = prQueue[-1]
#             if curr[0] <= prev[1]:
#                 prQueue[-1][1] = max(curr[1], prev[1])
#                 prQueue[-1][0] = min(curr[0],prev[0])
#             else:
#                 prQueue.append(curr)
#             prev = curr
#         return prQueue
        # print(prQueue)
        
        