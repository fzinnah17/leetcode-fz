class Solution(object):
    def floodFill(self, image, sr, sc, color):
        Rows = len(image)
        Cols = len(image[0])
        visited = set()
        sourceColor = image[sr][sc]
        def helper(row, col):
            if (
            row < 0
            or col < 0
            or row >= Rows
            or col >= Cols
            or (row,col) in visited
            or image[row][col] != sourceColor):
                return
            visited.add((row,col))
            image[row][col] = color
            helper(row + 1,col)
            helper(row - 1,col)
            helper(row,col + 1)
            helper(row,col - 1)
        helper(sr,sc)
        return image
        
            
        