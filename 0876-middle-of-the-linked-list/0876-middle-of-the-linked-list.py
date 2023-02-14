# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        https://www.ijrte.org/wp-content/uploads/papers/v8i4/D7296118419.pdf
        Binary search is inefficient to use in Linked List, YET we will try to do it
        """
        length = 0
        start = head 
        while start:
            length += 1
            start = start.next  
        mid = length//2
        left = 0
        while head:
            if left == mid:
                return head
            else:
                left += 1
                head = head.next
        return None
            
        
        # slow, fast = head, head
        # while fast and fast.next:
        #     slow = slow.next
        #     fast = fast.next.next
        # return slow
            
            
        
        