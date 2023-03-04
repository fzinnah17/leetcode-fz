# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        """
        TC: O(N), SC: O(N)
        """
        output = []
        if not root:
            return output
        curr = targetSum - root.val
        #leaf node
        if not root.left and not root.right:
            if curr == 0:
                return [[root.val]]
            else:
                return output
        #non leaf node/has children:
        if root.left or root.right:
            leftPath = self.pathSum(root.left, curr)
            rightPath = self.pathSum(root.right, curr)
        for path in leftPath + rightPath:
            output.append([root.val]+path)
        return output
        