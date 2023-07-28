# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getDirections(self, root, startVal, destVal):
        """
       Just like in the forest, in a binary tree, there are multiple paths connecting different nodes. We need to determine the point where the paths from the start node and the destination node begin to diverge. This point of divergence is exactly what we call the Lowest Common Ancestor (LCA) in our binary tree.

The LCA helps us to efficiently split the problem into two manageable parts. We can separately find the path from the start node to the LCA and the path from the LCA to the destination node. By doing this, we simplify our problem-solving approach and can analyze the two paths step by step.
By finding the LCA, we can narrow down our focus, making our solution more organized and efficient. Once we have the two paths, it becomes much easier to analyze them and extract the directions required to navigate from the start node to the destination node.
"""
        def dfs(node):
            if not node:
                return None
            if node.val in [startVal,destVal]:
                return node
            left = dfs(node.left)
            right = dfs(node.right)
            if left and right:
                return node
            return left or right
        found = dfs(root)
        
        def helper(curr, lookupNode):
            if not curr:
                return ""
            if curr.val == lookupNode:
                return ""
            if curr.left and curr.left.val == lookupNode:
                return "L"
            if curr.right and curr.right.val == lookupNode:
                return "R"
            leftPath = helper(curr.left, lookupNode)
            rightPath = helper(curr.right, lookupNode)
            
            if leftPath:
                return "L" + leftPath
            
            if rightPath:
                return "R" + rightPath
            
            return ""
            
        startPath = helper(found, startVal)
        endPath = helper(found, destVal)
        
        return len(startPath) * "U" + endPath
        