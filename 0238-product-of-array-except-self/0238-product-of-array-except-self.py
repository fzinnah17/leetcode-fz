class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        """
        Array and Hashing: Store all the data in a list and retrieve the data from the list
        for this problem, it is giving us an array, we have to return an array that for each ith place we have the product of other nums
        -> retrieve the products of others nums from the array
        
        Pseudocode:
        in =  [ 1, 2,  3, 4]
        out = [24, 12, 8, 6]
        
        regular prefix = [] -> [1] -> [1, 2] -> [1,2,3] -> [1,2,3, 4]
        regular postfix = [1,2,3,4] -> [2,3,4] -> [3,4] -> [4] -> []
        
        multiplied prefix = [1] -> -> [1,1*2 = 2] -> [1,2, 1*1*2*3 = 6] -> [1,2,6, 1*1*2*3*4 = 24]  
        -> [1,1,2,6,24]
        multiplied postfix = [1*2*3*4 = 24] -> [2*3*4 = 24] -> [3*4 = 12] -> [4] -> []  
        -> [24,24,12,4,1]
        
       [ 1,  1,  2,  6, 24]
           x   x   x   x
       [24, 24, 12, 4,   1]
       
       [24, 12, 8, 6]
       
       how to do this zigzag multiplication?
       
        """
        n = len(nums)
        preList = [1] * n
        postList = [1] * n
        
        for i in range(1,n):
            preList[i] = preList[i - 1] * nums[i - 1]
        
        for i in range(n - 2, -1, -1):
            postList[i] = postList[i+1] * nums[i + 1]
        
        result = []
        
        for i in range(n):
            result.append(preList[i] * postList[i])
        
        return result
            