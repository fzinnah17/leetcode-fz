# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        TC: O(n) SC: O(n)
        """
        rightSide = []
        currLevel = deque()
        if root:
            currLevel.append(root)
        while currLevel:
            rightNode = currLevel[-1]
            rightSide.append(rightNode.val)
            nextLevel = deque()
            for var in currLevel:
                if var.left:
                    nextLevel.append(var.left)
                if var.right:
                    nextLevel.append(var.right)
            currLevel = nextLevel            
        return rightSide
        