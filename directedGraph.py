"""
Question:
You are given a directed graph with n nodes and several edges. Each edge has a weight and connects two distinct nodes in one direction. You can get the details of the graph through these parameters:

g_nodes: The total number of nodes in the graph. The nodes are numbered sequentially from 1 to g_nodes.
g_from: An array of integers where g_from[i] indicates the starting node of the i-th edge.
g_to: An array of integers where g_to[i] indicates the ending node of the i-th edge.
g_weight: An array of integers where g_weight[i] indicates the weight of the i-th edge.

In addition to the given edges, you have the ability to add new edges between any pair of distinct nodes that are not already directly connected, with a weight of 1.

Your task is to determine the minimum possible weight of a path from node 1 to node g_nodes. The weight of a path is the sum of the weights of all edges traversed on that path.

Write a function minCost(g_nodes, g_from, g_to, g_weight) that takes these parameters as input and returns the minimum possible weight of a path from node 1 to node g_nodes.

Example 1:
Input:
g_nodes = 2
g_from = [1]
g_to = [2]
g_weight = [3]

Output: 3 (Explanation: There is already a direct edge from node 1 to node 2 with weight 3, which is the minimum cost path.)

Example 2:
Input:
g_nodes = 4
g_from = [1, 2, 1]
g_to = [2, 3, 4]
g_weight = [3, 2, 5]

Output: 3(Explanation: We can add an edge from node 3 to node 4 with weight 1. So, the minimum cost path is 1 -> 2 -> 3 -> 4, with a total weight of 3.)

Example 3:
Input: 

g_nodes = 4
g_from = [1, 2, 2, 3]
g_to = [2, 3, 4, 4]
g_weight = [2, 3, 6, 2]

Output: 3 (Explanation: We can add an edge from node 1 to node 4 with weight 1. So, the minimum cost path is 1 -> 4, with a total weight of 1.)

Example 4: Input:
g_nodes = 5
g_from = [1, 2, 3, 4, 1, 2]
g_to = [2, 3, 4, 5, 5, 4]
g_weight = [1, 2, 3, 4, 10, 5]

Output: 4(Explanation: We can add an edge from node 3 to node 5 with weight 1. So, the minimum cost path is 1 -> 2 -> 3 -> 5, with a total weight of 4.)

Pseudocode:
Initialize a graph where each node has a dictionary of its connected nodes and corresponding edge weights.

For each given edge, add it to the graph. If there are multiple edges between the same pair of nodes, keep the one with the smallest weight.

Initialize a distance array to keep track of the minimum distance from node 1 to each node. Also, initialize a priority queue with node 1 and a distance of 0.

While there are nodes in the priority queue:

Remove the node with the smallest distance from the queue.

If the current distance is greater than the recorded minimum distance, skip the current iteration.

For each other node in the graph, calculate the new distance from node 1. The cost is 1 if the nodes are not directly connected, and the actual edge weight if they are.

If the new distance is smaller than the recorded minimum distance, update the minimum distance and add the node to the priority queue.

Return the minimum distance to the last node.

The time complexity (TC) of the algorithm is O(V^2 log V), where V is the number of vertices (or nodes) in the graph. The V^2 term comes from the fact that for each node, we potentially iterate over all other nodes in the graph. The log V term is due to the use of a priority queue (implemented as a heap), which takes log V time for insertion and deletion.

The space complexity (SC) of the algorithm is O(V), which is the space required to store the graph (in the form of adjacency lists), the distances array, and the priority queue. Each of these data structures can potentially store an entry for each node in the graph, hence the space complexity is linear in the number of nodes.
"""

import heapq

def minCost(g_nodes, g_from, g_to, g_weight):
    INF = float('inf')
    edges = {i: {} for i in range(1, g_nodes+1)}
    
    # Step 1: Create the graph
    for i in range(len(g_from)):
        edges[g_from[i]][g_to[i]] = min(edges[g_from[i]].get(g_to[i], INF), g_weight[i])

    # Step 2: Initialize the distance array and priority queue
    distances = [INF] * (g_nodes + 1)
    distances[1] = 0
    pq = [(0, 1)]

    # Step 3: Dijkstra's algorithm
    while pq:
        cost, node = heapq.heappop(pq)
        if cost > distances[node]:
            continue
        for i in range(1, g_nodes+1):
            if i == node:
                continue
            nextCost = cost + edges[node].get(i, 1)
            if nextCost < distances[i]:
                distances[i] = nextCost
                heapq.heappush(pq, (nextCost, i))
    
    # Step 4: Return the shortest distance to the last node
    return distances[g_nodes]
