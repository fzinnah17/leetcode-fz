# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            #cycle found
            if slow == fast:
                break
        else:
            return
        
        temp = head
        while temp != slow:
            temp = temp.next
            slow = slow.next
        #as soon as temp and slow meets
        return temp
        