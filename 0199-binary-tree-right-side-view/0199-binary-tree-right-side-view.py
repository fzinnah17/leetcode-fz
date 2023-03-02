# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def rightSideView(self, root):
        """
        TC + SC: O(N)
        """
        queue = collections.deque()
        queue.append(root)
        output = collections.deque()
        if not root:
            return output
        while queue:
            for i in range(len(queue)):
                node= queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(node.val)
        return output
                
        
        