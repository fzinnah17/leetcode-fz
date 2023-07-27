class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        Edge case:
        n < 2: return the length
        """
        if n <= 2:
            return [i for i in range(n)]

        adjList = defaultdict(set)
        for edge in edges:
            adjList[edge[0]].add(edge[1])
            adjList[edge[1]].add(edge[0]) #node neighbor

        leafNodes = []
        for i in range(n):
            if len(adjList[i]) == 1:
                leafNodes.append(i)

        remNodes = n
        while remNodes > 2:
            remNodes -= len(leafNodes)
            newLeaves = []
            while leafNodes:
                eachLeaf = leafNodes.pop()
                neighbor = adjList[eachLeaf].pop() #removing from the dictionary but we are keeping track of it
                adjList[neighbor].remove(eachLeaf) #removing from the dictionary
                if len(adjList[neighbor]) == 1:
                    newLeaves.append(neighbor)
            leafNodes = newLeaves
        return leafNodes
        