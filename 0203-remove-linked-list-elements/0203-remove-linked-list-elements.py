# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        temp = ListNode()
        temp.next = head
        # print(temp)
        prev = temp
        
        while head:
            if head.val == val:
                prev.next = head.next
            else:
                #change the positions
                prev = head
            head = head.next
                
        return temp.next
        
        