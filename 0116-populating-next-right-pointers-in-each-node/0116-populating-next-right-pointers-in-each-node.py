"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
    IMP : The first while loop iterates over each level one by one, while the inner for loop iterates over all nodes on that level.
"""

class Solution(object):
    def connect(self, root):
        queue = collections.deque()
        queue.append(root)
        if not root:
            return None
        while queue:
            nodeVal = queue.popleft()
            if nodeVal.left and nodeVal.right:
                nodeVal.left.next = nodeVal.right
            if nodeVal.right and nodeVal.next:
                nodeVal.right.next = nodeVal.next.left #5(right node's next) is pointing to 6([pointer==next]left)
            if nodeVal.left:
                queue.append(nodeVal.left)
            if nodeVal.right:
                queue.append(nodeVal.right)
        return root
        """
        Brute Force: 
            1. We can add (node,level) pairs to the queue, and when we add a node's children, we add (node.left,parent level+1), and (node.right,parent level+1). Our algorithm doesn't work well with this method because we need all nodes to be on the same level, which requires an additional data structure.
            2. Putting something between the levels is a more memory-efficient way to separate nodes on the same level. We usually put a NULL entry in the queue to mark the end of one level and the beginning of the next. This is a great idea, but again, it would still use some memory based on how many levels there are in the tree.
        
        Optimized:
        To avoid using a NULL pointer, we'll use a nested loop structure in this approach. Basically, at each step, we write down the queue size, which is always the same for all nodes on a given level. We only process this many elements when we reach the size. When we're done processing the size number of elements, the queue will contain all of the nodes on the next level.
        BFS algorithm approach using queue
        1. queue
            a. add the root
        2. edge case: empty ---> []
        3. while queue:
            a. remove the node
        4. Add left and right children
        
            
        """
        