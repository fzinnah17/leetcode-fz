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
        TC : O(N) we visit each node exactly once
        SC: BEST: (if the tree is perfectly balanced), the height of the tree would be log(N). So, the space complexity in this case would be O(log(N))
            WORST: the tree is completely unbalanced, meaning that each node has only one child node. In this case, the recursion call would happen N times (the height of the tree), so the storage needed to keep the call stack would be O(N).
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
        
        