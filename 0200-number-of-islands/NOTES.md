1. Representing a matrix: This problem is giving a grid or matrix, which is shown as a 2D array. Each cell in the matrix is representing a specific value [1 or 0] depending on the state [land or water].
2. Preprocessing: Simplify?????
3. Boundaries/Edge cases: [r: 1,c:1], [r: 1, c: len- 1], [r: len - 1, col: 1], [r: len-1, col: len-1]
to make sure I don't leave the matrix.
0 -> water -> not allowed to move
4. Grid Constraints: not traversed diagonally
5. Traversal of the matrix: left, right, up, or down,
6. Direction Arrays: Instead of writing different code for each traversal direction, I can save the possible movement offsets in direction arrays.
7. Visited Cells: Keep track of the cells I've been to so I don't end up stuck in a loop by going back to them.
8. Marking Visited Cells: Use a separate visited array or change the matrix itself by marking visited cells
9. Connected Components: Find and count the number of connected 1's.
10. Matrix Connectivity: Figure out if all the cells [1] in the matrix are connected or how many different parts are connected. Consider using DFS or BFS to see how cells are linked.
11. Counting Islands: Use a counter variable to keep track of how many islands are seen during traversal. Add one to the counter each time a new island is found.
12. DFS/BFS?: DFS because for each cell we can check each direction, and come back to the original cell to check if there are any other direction left to check
13. Recursive Backtracking: Look at all the choices, make a decision, and go back if you need to.
14. Matrix Search: Changing the traversal path if 0 is seen.