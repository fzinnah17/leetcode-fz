# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        pointerOne = headA
        pointerTwo = headB
        
        while pointerOne != pointerTwo:
            pointerOne = headB if pointerOne is None else pointerOne.next
            pointerTwo = headA if pointerTwo is None else pointerTwo.next
        return pointerTwo
            