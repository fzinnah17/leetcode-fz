# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #an empty node we are making
        temp = None
        
        while head:
            #pointer pointing at 2
            nxt = head.next
            #1 will remove it's pointer from 2 and redirect it to null/empty node
            head.next = temp
            #shift the positions
            temp = head
            head = nxt
        return temp
            
        