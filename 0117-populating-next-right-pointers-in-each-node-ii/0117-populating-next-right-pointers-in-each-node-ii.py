"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution(object):
    def connect(self, root):
        """
        :type root: Node
        :rtype: Node
        TC + SC: O(n)
        """
        queue = collections.deque()
        queue.append(root)
        if not root:
            return None
        while queue:
            level = len(queue)
            prev = None
            while level:
                nodeVal = queue.popleft()
                level -=1
                if nodeVal.left:
                    queue.append(nodeVal.left)
                if nodeVal.right:
                    queue.append(nodeVal.right)
                if prev:
                    prev.next = nodeVal
                prev = nodeVal
            prev.next = None
        return root