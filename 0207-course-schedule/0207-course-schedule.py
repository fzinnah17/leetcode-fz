class Solution:
    def canFinish(self, numCourses: int, prereq: List[List[int]]) -> bool:
        
        visited = set()
        graph = collections.defaultdict(list)
        for crs, pre in prereq:
            graph[crs].append(pre)
            
        def dfs(crs):
            
            if crs in visited:
                return False
            
            if graph[crs] == []:
                return True
        
            visited.add(crs)
            
            for child in graph[crs]:
                if not dfs(child):
                    return False
            
            graph[crs] = []
            visited.remove(crs)
            return True
        
        for i in range(numCourses):
            if not dfs(i):
                return False
        
        return True