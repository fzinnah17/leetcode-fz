"""
Nam is an employee who has been assigned a number of tasks to complete. However, there are some dependencies between the tasks i.e., some tasks must be completed before others. Given these dependencies, help Nam determine the maximum number of tasks he can complete.

Specifically, you're given n tasks numbered from 1 to n and two lists of equal length a and b, representing the dependencies. If a[i] and b[i] is a pair, it means task b[i] cannot be completed before task a[i].

However, if there is a circular dependency i.e., a task i depends on task j and task j also depends on task i, then Nam can only complete one of the tasks. Determine the maximum number of tasks that Nam can complete.

Example 1:
n = 7
a = [1,2,3,4,6,5]
b = [7,6,4,1,2,1]
print(tasks(n, a, b)) # Expected output: 6

Example 2:
n = 2
a = []
b = []
print(tasks(n, a, b)) # Expected output: 2

Example 3:
n = 5
a = [1,2,3,4]
b = [2,3,4,5]
print(tasks(n, a, b)) # Expected output: 5

Example 4:
n = 10
a = [1,2,3,4,5,6,7,8,9,10]
b = [2,3,4,5,6,7,8,9,10,1]
print(tasks(n, a, b)) # Expected output: 9

Pseudocode:

Construct a graph based on the dependencies.
Detect if there are any cycles in the graph.
If there are cycles, return the total number of tasks minus the number of cycles.
If there are no cycles, return the total number of tasks.

Time Complexity: O(n) - we are visiting each node once.
Space Complexity: O(n) - for storing the graph and visited list.
"""

from collections import defaultdict, deque

def tasks(n, a, b):
    graph = defaultdict(list)
    visited = [0 for _ in range(n+1)]
    cycles = 0
    
    # build the graph
    for i in range(len(a)):
        graph[b[i]].append(a[i])

    # DFS traversal to detect cycles
    def dfs(node):
        if visited[node] == -1: # cycle detected
            return True
        if visited[node] == 1: # already visited and no cycle
            return False
        visited[node] = -1 # mark as being visited
        for nei in graph[node]:
            if dfs(nei):
                return True
        visited[node] = 1 # mark as visited
        return False
    
    # run dfs on all nodes
    for i in range(1, n+1):
        if visited[i] == 0 and dfs(i):
            cycles += 1

    return n - cycles
