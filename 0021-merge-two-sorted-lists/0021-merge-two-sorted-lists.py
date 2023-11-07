# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        #TC: O(n) SC: O(1)
        
        prev, top, bottom = None, list1, list2
        
        if not top:
            return bottom
        if not bottom:
            return top
        
        if top.val < bottom.val:
            prev = top
            top = top.next
        else:
            prev = bottom
            bottom = bottom.next
        
        head = prev
        
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
            
        