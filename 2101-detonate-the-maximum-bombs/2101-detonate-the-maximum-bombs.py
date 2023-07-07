class Solution:
    def maximumDetonation(self, bombs):
        """"""
        # Depth-First Search (DFS) function to traverse the graph
        def dfs(graph, visited, count, i):
            # Mark the current node as visited
            visited[i] = True
            # Increment the count of visited nodes
            count[0] += 1
            # Explore neighbors of the current node
            for j in graph[i]:
                # If the neighbor is not visited, recursively call the DFS function
                if not visited[j]:
                    dfs(graph, visited, count, j)
        
        # Get the number of bombs
        n = len(bombs)
        # Create an empty graph to represent the relationships between bombs
        graph = [[] for _ in range(n)]
        
        # Build the graph by checking the distance between each pair of bombs
        for i in range(n):
            x1, y1, r1 = bombs[i]
            for j in range(n):
                if i != j:
                    x, y = bombs[j][0], bombs[j][1]
                    # Calculate the squared distance between two bombs using the coordinates
                    distance_sq = (x - x1) ** 2 + (y - y1) ** 2
                    # If the distance is within the range of the bomb's detonation radius, add an edge in the graph
                    if distance_sq <= r1 ** 2:
                        graph[i].append(j)
        
        # Initialize the maximum detonation count as negative infinity
        max_detonation = float('-inf')
        # Traverse each bomb as a starting point for DFS to find the maximum detonation count
        for i in range(n):
            count = [0]  # Initialize the count of visited nodes
            visited = [False] * n  # Create an array to keep track of visited nodes
            dfs(graph, visited, count, i)  # Perform DFS starting from the current bomb
            # Update the maximum detonation count if necessary
            max_detonation = max(max_detonation, count[0])
        
        # Return the maximum detonation count
        return max_detonation
