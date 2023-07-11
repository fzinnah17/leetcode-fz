# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isBalanced(self, root):
        """
        Balanced Tree:
        difference between the subtrees should not exceed more than 1: return True otherwise False
        TC: O(n), where n is the number of nodes in the tree.
        SC: O(n) in the worst case if the tree is completely unbalanced, and the maximum depth of the call stack is equal to the height of the tree.
        """
        if not root:
            return True   
        def dfs(node):
            if not node:
                return 0
            leftHeight = dfs(node.left)
            rightHeight = dfs(node.right)
            return max(leftHeight,rightHeight) + 1
        leftHeight = dfs(root.left)
        rightHeight = dfs(root.right)
        
        if self.isBalanced(root.left) and self.isBalanced(root.right) and abs(leftHeight - rightHeight) <= 1:
            return True
        return False
        
        