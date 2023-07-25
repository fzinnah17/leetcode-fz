"""
You have a graph with n nodes. You are given an integer n and an array of edges, with edges [i] = [ai, bi] indicating that an edge exists in the graph between a; and b;.
The number of connected graph components is returned.

n = 10
edges = [[0, 1], [1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7], [7, 8], [8, 9]]
Output = 6

TC: O(N) SC: O(N)
"""
from collections import defaultdict
def countComponents(n, edges):
    visited = set()
    output = 0
  #creating the adjacency list of the undirected graph
    def buildList(edges):
        adjList = defaultdict(list)
        for e in edges:
            a,b = e
            adjList[a].append(b)
            adjList[b].append(a)
        return adjList
    adjList = buildList(edges)
  #helper function to iterate through the adjacency list
    def dfs(vertex):
        visited.add(vertex)
        for neighbor in adjList[vertex]:
            if neighbor not in visited:
                dfs(neighbor)
    for v in range(n):
        if v not in visited:
            dfs(v)
            output += 1
    return output
