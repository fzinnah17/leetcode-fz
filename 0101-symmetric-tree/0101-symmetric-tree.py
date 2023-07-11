# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        TC: O(n) number of nodes
        SC: O(h) recursion stack space/ height of the tree
        """
        def dfs(nodeLeft, nodeRight):
            if not nodeLeft and not nodeRight:
                return True
            elif not nodeLeft or not nodeRight:
                return False
            elif nodeLeft.val != nodeRight.val:
                return False
            else:
                return dfs(nodeLeft.left, nodeRight.right) and dfs(nodeLeft.right, nodeRight.left) #recursively call the function on the left and right children
        if root:
            return dfs(root.left, root.right)