class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        end_node = len(graph) - 1
        
        def dfs(node, path, result):
            
            if node == end_node:
                result.append(path)
                
            for neighbour in graph[node]:
                dfs(neighbour, path + [neighbour], result)
                
        result = []
        dfs(0, [0], result)
        return result
        