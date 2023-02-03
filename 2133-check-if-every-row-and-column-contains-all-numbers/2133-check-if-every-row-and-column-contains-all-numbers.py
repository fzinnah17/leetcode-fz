class Solution(object):
    def checkValid(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: bool
        1. bounds: upper and lower [For Matrix, the last pointer is the final value third row bottom right last element, FORMULA: rows*cols-1]
        2. iteration
        3. For any 2D, 
            a. To print each element of Matrix/ 2D matrix iteration format:
                for i in range(len(data)):
                    for j in range(len(data[i])):
                        print(data[i][j], " ")
            b. Rows = len(grid) [[[- 1]]], Cols = len(grid[0]) [[[[- 1]]]] -1 MIGHT OR MIGHT NOT NEEDED
            c. currRow = middle // cols
               currCol = middle % cols  {{{{THESE ARE THE FORMULAS TO FIND CURRENT POSITION}}}}
        """
        # row, n = len(matrix), len(matrix)
        # col = len(matrix[0])
        # for i in range(row):
        #     rowSet = set()
        #     for j in range(col):
        #         rowSet.add(matrix[j][i])
        # print(rowSet)
        for i in matrix:
            if len(i) != len(set(i)):
                return False
        
        for i in range(len(matrix)):
            matrixSet = set()
            for j in range(len(matrix)):
                matrixSet.add(matrix[j][i])
            if len(matrixSet) != len(matrix):
                return False
            # print(matrixSet)
        return True
            
            # print(i, " ", (set(i))) 
            # -------> ([1, 1, 1], ' ', set([1]))       :   3 , 1
            #          ([1, 2, 3], ' ', set([1, 2, 3])) :   3 , 3
            #          ([1, 2, 3], ' ', set([1, 2, 3])) :   3 , 3
        
        # for i in range(len(matrix)):
        #     hashSet = set(matrix[i])
        # #print(hashSet)  -------> set([1, 2, 3])
        # #-------> set([1, 2, 3, 4])
        #     for j in range(len(matrix[0])):
        #         matrixSet = set(matrix[j])
        # #print(matrixSet) -------> set([1, 2, 3])
        # # #-------> set([1, 2, 3, 4])
        # if hashSet == matrixSet:
        #     return True
        # return False

        