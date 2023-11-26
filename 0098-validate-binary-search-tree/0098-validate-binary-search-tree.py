# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        ans = []
        
        #in order traversal
        
        def dfs(node):
            #base case -> leaf node
            if not node:
                return
            
            if node.left:
                dfs(node.left)
            #add the current node values
            ans.append(node.val)
                #backtrack
            if node.right:
                dfs(node.right)                
        dfs(root)
        
        for i in range(1, len(ans)):
            if ans[i] <= ans[i - 1]:
                return False
        return True
    
    """
    Time: O(n) 
    Space: O(n)
    """
            
        