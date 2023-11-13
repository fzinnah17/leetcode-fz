class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        adjList = collections.defaultdict(list)
        for node in range(len(graph)):
            adjList[node] = graph[node]

        target = len(graph) - 1
        results = []

        def dfs(node, path):
            if node == target:
                results.append(path.copy())
                return
            
            for next_node in adjList[node]:
                path.append(next_node)
                dfs(next_node, path)
                path.pop()

        dfs(0, [0])
        return results
        