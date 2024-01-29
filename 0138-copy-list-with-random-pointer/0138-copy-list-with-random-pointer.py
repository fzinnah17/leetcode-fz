"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        # Create nodes
        mapLL = {}
        tmp = head
        while tmp:
            mapLL[tmp] = Node(tmp.val)
            tmp = tmp.next

        # Attach pointers
        tmp = head
        while tmp:
            node = mapLL[tmp]
            node.next = mapLL.get(tmp.next)
            node.random = mapLL.get(tmp.random)
            tmp = tmp.next

        return mapLL[head]

        