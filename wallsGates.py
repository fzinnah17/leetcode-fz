"""
A m x n grid of rooms with three possible values is presented to you.

-1 A stumbling block or a wall.
0 A gate.
INF Infinity represents an infinite amount of space. Because the distance to a gate is likely to be less than 2147483647, we chose the value 231 - 1 = 2147483647 to represent INF.
In each empty room, enter the distance to the nearest gate. If it is impossible to reach a gate, it should be filled with INF.

rooms = [
    [2147483647, -1, 0, 2147483647, 2147483647, 0],
    [2147483647, -1, 2147483647, -1, 2147483647, 2147483647],
    [2147483647, -1, 2147483647, -1, -1, 2147483647],
    [0, 2147483647, 2147483647, 2147483647, 0, -1],
    [-1, 2147483647, 2147483647, -1, 2147483647, 2147483647],
    [2147483647, -1, -1, 2147483647, -1, 2147483647]
]
Output:
[[3, -1, 0, 1, 2, 0],
 [2, -1, 1, -1, 1, 1],
 [1, -1, 2, -1, -1, 2],
 [0, 1, 1, 1, 0, -1],
 [-1, 2, 2, -1, 1, 1],
 [1, -1, -1, 2, -1, 2]]

Instead of returning anything, adjust the rooms in-place.
"""

def wallsGates(rooms):
  numRows = len(rooms)
  numCols = len(rooms[0])

  def dfs(r, c, distance):
    if (r < 0 or c < 0 or r >= numRows or c >= numCols or rooms[r][c] == -1 or rooms[r][c] < distance):
      return
    rooms[r][c] = distance
    dfs(r + 1, c, distance + 1)
    dfs(r - 1, c, distance + 1)
    dfs(r, c + 1, distance + 1)
    dfs(r, c - 1, distance + 1)
  for r in range(numRows):
    for c in range(numCols):
      if rooms[r][c] == 0:
        dfs(r, c, 0)
  return rooms
"""
TC: O(n * m),  n is the number of rows and m is the number of columns in the grid. This is because in the worst case, we might need to visit all the cells in the grid to find the distance to the nearest gate.
SC: O(n * m), the algorithm uses additional memory for the visited set and the stack used for DFS. In the worst case, the visited set can contain all the cells in the grid (in case there are no walls or gates, and all cells are INF).
"""
