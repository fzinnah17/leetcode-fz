# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        #manipulate the references of the nodes -> two pointer
        #take two pointers one at head and other at NULL position intially and we slowly reverse the point position at each point using a temp variable and solve the problem using normal iteration
        prev = None
        curr = head
        
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        return prev
        
        
        