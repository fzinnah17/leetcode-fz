# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        1. queue [add root]
        2. minDepth = 0
        3. Queue value exists ----> loop thru
            currLevel = 0
            traverse thru the remaining values of the queue
            pop the node value
            level += 1
        4. Add left and right children
        5. find max (minDepth, level)
        6. return mindepth
        TC + SC: O(n)
        """
        
        queue = collections.deque()
        queue.append(root)
        minDepth = 0
        if not root:
            return 0
        while queue:
            minDepth += 1
            for i in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if not node.left and not node.right:
                    return minDepth
        
        