# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        queue = collections.deque()
        output = collections.deque()
        queue.append(root)
        oddLevel = True
        if not root:
            return output
        while queue:
            subLists = collections.deque()
            for i in range(len(queue)):
                node = queue.popleft()
                if oddLevel:
                    subLists.append(node.val)
                else:
                    subLists.appendleft(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.append(subLists)
            oddLevel = not oddLevel
        return output
            
                
                
        
        