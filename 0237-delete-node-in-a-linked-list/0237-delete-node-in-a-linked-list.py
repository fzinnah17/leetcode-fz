# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def deleteNode(self, node):
        """
        KeyPoints:
        1. Singly linked list: access to the next node only
        2. Not given access to the first node 'head'
        3. Values of the linked list are unique
        
        Task: Delete a given node 'node'
        TC: O(1) SC: O(1)"""

        # Copy the value of the next node to the given node
        node.val = node.next.val

        # Skip the next node by updating the pointers
        node.next = node.next.next

                
        
        
        