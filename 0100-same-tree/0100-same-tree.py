# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSameTree(self, p, q):
        """
        """
        if not p and not q:
            return True
        if not p or not q:
            return False
        
        queueOne = collections.deque([p])
        queueTwo = collections.deque([q])
        
        while queueOne and queueTwo:
            nodeOne = queueOne.popleft()
            nodeTwo = queueTwo.popleft()
            if not nodeOne and not nodeTwo:
                continue
            elif not nodeOne or not nodeTwo:
                return False
            elif nodeOne.val != nodeTwo.val:
                return False
            queueOne.append(nodeOne.left)
            queueOne.append(nodeOne.right)
            queueTwo.append(nodeTwo.left)
            queueTwo.append(nodeTwo.right)
        return True
        
            
        
        