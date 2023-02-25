# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrderBottom(self, root):
        """
        TC + SC: O(n)
        """        
        queue = collections.deque()
        queue.append(root)
        output = collections.deque() #appendleft is a propert of queue so need to use deque for the output. Otherwise, I have to reverse the list at the end
        if not root:
            return []
        while queue:
            subLists = []
            for i in range(len(queue)):
                node = queue.popleft()
                subLists.append(node.val)        
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            output.appendleft(subLists)
        return output
                    
                    
            
        