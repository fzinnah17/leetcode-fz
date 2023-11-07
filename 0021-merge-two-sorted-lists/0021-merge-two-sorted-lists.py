# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1Head: Optional[ListNode], list2Head: Optional[ListNode]) -> Optional[ListNode]:
        #top pointer = list1head
        #bottom pointer = list2head
        #while both exists: compare the values of both list nodes
        #if l1 == l2: move the l1 pointer
        #if l1 > l2: 
        prev = None
        top = list1Head
        bottom = list2Head
        
        #edge cases:
        if not top:
            return bottom
        if not bottom:
            return top
        
        #which list to start from?
        if top.val < bottom.val:
            prev = top
            top = top.next
        else: #top.val => bottom.val
            prev = bottom
            bottom = bottom.next #change the position
        head = prev #Return the head of the merged linked list.
        
        while top and bottom:
            if top.val <= bottom.val:
                temp = top.next
                prev.next = top
                prev = top
                top = temp
                
            else:
                temp = bottom.next
                prev.next = bottom
                prev = bottom
                bottom = temp
        
        if top:
            prev.next = top
        else:
            prev.next = bottom
        return head
            
            
                