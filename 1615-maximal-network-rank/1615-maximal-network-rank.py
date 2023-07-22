class Solution(object):
    def maximalNetworkRank(self, n, roads):
        """
        :type n: int
        :type roads: List[List[int]]
        :rtype: int
        0 : [1,3]
        1 : [0, 2, 3]
        2:  [1, 3, 4]
        3:  [0, 1, 2]
        """
        maxRank = 0
        roadList = defaultdict(set)
        for road in roads:
            roadList[road[0]].add(road[1])
            roadList[road[1]].add(road[0])

        for node in range(n):
            for node1 in range(node +1, n):
                curr_rank = len(roadList[node]) + len(roadList[node1])
                if node1 in roadList[node]:
                    curr_rank -= 1
                maxRank = max(maxRank, curr_rank)
        return maxRank
        