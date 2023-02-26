# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        TC + SC: O(n)
        Pseudocode:
            1. Use BFS ----> deque() to have leverage for FIFO and FILO.
            2. Edge cases: empty
            3. Append root to queue and traverse to find the subLists.
                a. node val
                        i. odd Level -----> LefttoRight
                        ii. even Level -----> RighttoLeft
                b. Add the children
            4. Add the sub-lists in the output list
            5. reverse the 
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
            output.append(subLists) # [[3],[9,20],[15,7]]
            oddLevel = not oddLevel #after reversing [[3],[20,9],[15,7]]
        return output 
            
                
                
        
        