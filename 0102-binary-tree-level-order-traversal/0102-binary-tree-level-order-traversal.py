# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def levelOrder(self, root):
        """
        Pseudocode:
        ***EDGE CASES ----> [] [ROOT]***
        1. Initialize a queue[FIFO]
        2. Add the root/
        3. As long as the root exists in a deque, we can loop
        4. As we are in the queue, we can get the Level size. [the size is not fixed and changes according to the node size]
                        a. Remove the node from the queue
                        b. Insert the node value from the queue in a list
                        c. If there is any children, then add it in the back of the queue
                Repeat this process till the traversal is done for the tree
        5. Add the sublists into the actual final list
        6. Return the final list           
        """
        if not root:
            return []
        deque = collections.deque()
        deque.append(root)
        output = []
        
        while deque: #because now the deque has the root in it
            subList = []
            for _ in range(len(deque)):
                node = deque.popleft()
                subList.append(node.val)
                
                if node.left:
                    deque.append(node.left)
                if node.right:
                    deque.append(node.right)
            output.append(subList)
        return output
                    
            
            
            
        