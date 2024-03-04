# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr and curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next
        return head
"""
      Fred's way
      [1,1,2,3,3]
      h
         s
         f
         
      slow = fast = head
      
      while slow and fast:
        while fast and slow.val == fast.val:
          fast = fast.next
        slow.next = fast
        slow = fast
        
      return head
"""
        