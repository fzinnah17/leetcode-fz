"""
You have an n-node graph with labels ranging from 0 to n -1. You are given an integer n and a list of edges, with edges[i] = [ai, bi] indicating that an undirected edge exists in the network between nodes ai and bi.

Return true if the edges of the provided graph form a valid tree, otherwise return false.

   0
  / \
 1   2
 |   |
 3   5
 |  / \
 7 9   6
 | |
 8 |
  \|
   4

n = 10
edges = [[0, 1], [0, 2], [1, 3], [1, 4], [2, 5], [2, 6], [3, 7], [3, 8], [4, 9], [5, 9], [6, 7], [7, 8]]

Output = True

Input:
n = 17
edges = [[0, 1], [1, 2], [2, 3], [3, 0], [4, 5], [5, 6], [6, 7], [7, 4], [8, 9], [9, 10], [10, 11], [11, 8], [12, 13], [13, 14], [14, 15], [15, 16], [16, 12], [3, 4], [7, 8], [11, 12]]

Output:
False

TC: O(n) SC: O(n)
"""

from collections import defaultdict
def validGraph(n, edges):
    visited = set()
  #building the adjacency list for the given graph
    def buildList(edges):
        adjList = defaultdict(list)
        for e in edges:
            a,b = e
            adjList[a].append(b)
            adjList[b].append(a)
        return adjList
    adjList = buildList(edges)
    #helper function to implement on each node of the graph
    def dfs(node,parent):
        if node in visited: # There is a cycle in the graph
            return False
        #if we couldn't find the node in the set, then add it
        visited.add(node)
        
        for neighbor in adjList[node]:
            if neighbor == parent:
                continue # Skip the parent node in an undirected graph
            #else
            #Recursively call the dfs function for each neighbor, here node becomes the parent
            if not dfs(neighbor,node):
                return False
        return True
    if not dfs(0,-1): #the starting node is 0th index and it has no parent so it is -1 for the parent and we will return False for that
        return False
    return len(visited) == n #as long as visited nodes are same as the given n we are returning True
