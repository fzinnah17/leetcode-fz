class Solution(object):
    def shortestPath(self, grid, k):
        #we are gonna iterate through each of the lists and then we can have something for up, down, left, right
        #set to check if any tie has been already visited so that we dont go back
        #this grid is an undirected graph
        #learn how to implement BFS in grid
        
        rows = len(grid) # print(rows) 5
        cols = len(grid[0]) # print(cols) 3
        target = (rows - 1, cols - 1) # print(target) (4, 2)
        
        #edge case: if no obstacle is there OR what if it was full of obstacles and k had capacity to remove all those obstacles
        
        if k >= (rows - 1) + (cols - 1): # 4 + 2 = 6,    k >= 6
            return rows + cols - 2 #5 + 3 -2 = 6 #6 steps
        
        queue = collections.deque([(0,(0,0,k))]) #0 = total number of steps are taken, () = tuple that represents the current state of our path[current row, current column, current number of obstacle used]
        
        seen = set([(0,0,k)]) #rows, columns, k that we removed
         
        directions = [(0,1), (0,-1), (-1,0), (1,0)] #up, down, left, right
        
        while queue:
            steps, (curr_row, curr_col, removals) = queue.popleft() # remove and return left most element from the queue
            
            if (curr_row, curr_col) == target:
                return steps
            
            for row_inc, col_inc in directions:
                new_row = curr_row + row_inc
                new_col = curr_col + col_inc
                
                #what if it is out of bound like no left, right, up, down
                if (0 <= new_row < rows) and (0 <= new_col < cols): #this makes it a valid position
                    #check if the current tile has any obstacles
                    new_removals = removals - grid[new_row][new_col] #each obstacle value is 1, if no obstacle is there then new removal is same as the previous one as the value is 0
                    new_state = (new_row,new_col,new_removals)
                    #check if removals is > 0
                    if new_removals >= 0 and new_state not in seen: #means we still need to explore
                        seen.add(new_state)
                        queue.append((steps+1, new_state))
        return -1
    #TC: O(n)*k SC: O(n)*k [keep track of k possible paths]
    #worst case is visiting all tiles so this O(n), we can visit it upto k times
    
                    
                    
                
        
        
        
        
        
        
        
        
        
        
        
        