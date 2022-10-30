"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child
"""

class Solution(object):
    def flatten(self, head):
        #The idea is to iterate through the linked list and keep on iterating for the next pointer, but also to check if there is any child node of any of the nodes. If there is any child node, then we have to check if there is any next value of that node. If so, then the next linked list values will go to the stack. Then, the head.next pointer will become the children values. Also, the children value's previous value will be the head. After we are completely done iterating through the linked list, we will take out the value from the stack one at a time from the end and later on return the head.
        
        stack = []
        start = head
        
        while head:
            if head.child:
                if head.next:
                    stack.append(head.next)
                head.next = head.child
                head.next.prev = head
                head.child = None
            if head.next == None and len(stack) != 0:
                head.next = stack.pop()
                head.next.prev = head
            head = head.next
        return start
        