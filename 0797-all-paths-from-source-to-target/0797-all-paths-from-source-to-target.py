class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        """
        example 1: [node 0 -> [4,3,1],
                    node 1 -> [3,2,4],
                    node 2 -> [3],
                    node 3 -> [4],
                    node 4 -> [] target so it is blank? len(graph) - 1]
        example 2: [node 0 -> [1,2],
                    node 1 -> [3],
                    node 2 -> [3],
                    node 3 -> [] target so it is blank? len(graph) - 1] 
        "We start at node 0 and explore each node connected to it. For each node, we add it to our path and call DFS recursively. If we reach the target node, we add the current path to our results. Then, we backtrack by removing the last node from our path and trying other paths."
        """
        adjList = collections.defaultdict(list) #automatic list creation for keys
        for node in range(len(graph)): 
            #gives us defaultdict(<class 'list'>, {0: [1, 2], 1: [3], 2: [3], 3: []})
            adjList[node] = graph[node] #key = node, value = graph[node] aka lists -> list of nodes that 'node' can reach
        target = len(graph) - 1 #last node in the graph
        results = []

        def dfs(node, path): # DFS function to explore all paths.
            #this only when we reach the last node
            if node == target:
                results.append(path.copy()) #add a copy of the current path results.
                #TC: O(n), N is number of elements in the list
                return
            #can this for loop below inside an else statement?
            for next_node in adjList[node]:
                path.append(next_node) #adds the next node of the current node to path
                dfs(next_node, path) #does the same recursion for the next node as well
                path.pop() #removes the last element from the path, allowing backtracking to explore all possible paths without getting stuck on one.

        dfs(0, [0])
        return results
"""    Time: O(2^N)*n because we explore every possible path,  and the number of paths in a graph can grow exponentially with the number of nodes.
    Space complexity: O(2^N * N), considering the space for storing all paths and the recursion stack."""
        