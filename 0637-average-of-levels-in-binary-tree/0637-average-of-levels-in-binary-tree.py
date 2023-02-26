# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def averageOfLevels(self, root):
        """
        TC + SC: O(n)
        """
        output = collections.deque()
        queue = collections.deque()
        queue.append(root)
        
        if not root:
            return output
        while queue:
            subLists = collections.deque()
            for i in range(len(queue)):
                node = queue.popleft()
                subLists.append(float(node.val))
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append((sum(subLists)) / (len(subLists)))
        return output
        