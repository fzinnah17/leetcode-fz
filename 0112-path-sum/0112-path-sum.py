# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def hasPathSum(self, root, targetSum):
        """
        PSEUDOCODE:
        1. Edge case: no root
        2. Check if leaf node
                a. check if equal to target OR curr = 0 TRUE
                B. check if not equal to target OR curr != 0 FALSE
        2. If NOT leaf node,
                a. call recursion on left children and right children
        """
        if not root:
            return False
        curr = targetSum - root.val
        if not root.left and not root.right: #leaf node
            if curr == 0:
                return True
            return False
        if root.left or root.right: #has children
            return self.hasPathSum(root.left, curr) or self.hasPathSum(root.right, curr)
        
        