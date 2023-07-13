# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        TC: O(n) SC: O(h)
        """
        rightSide = []
        
        def helper(node,level,rightSide):
            if not node:
                return
            
            if level == len(rightSide):
                rightSide.append(node.val)
            
            helper(node.right,level+1,rightSide)
            helper(node.left,level+1,rightSide)
        
        helper(root,0,rightSide)
        return rightSide
        
        
        