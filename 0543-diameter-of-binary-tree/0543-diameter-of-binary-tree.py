# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        # Create function to return the height of tree and collect diameter at each node
        def getDiameterOfBinaryTree(root: Optional[TreeNode]) -> int:
            nonlocal diameter
            # Basecase is a Null Node, return 0
            if not root:
                return 0

            # Collect information regarding diameter of node
            leftHeight = getDiameterOfBinaryTree(root.left)
            rightHeight = getDiameterOfBinaryTree(root.right)
            diameter = max(diameter, leftHeight + rightHeight)

            # Recursively return the max between height of left node and right node and add one for current node
            return max(leftHeight, rightHeight) + 1

        # Create variable to hold diameter information
        diameter = 0

        # Call the function to check diameter of each node
        getDiameterOfBinaryTree(root)

        # Return the diameter
        return diameter      