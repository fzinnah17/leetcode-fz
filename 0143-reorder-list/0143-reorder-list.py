# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        def reverseList(head):
            prev = None
            curr = head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev 
        def midElement(head):
            length = 0
            start = head
            while start:
                length += 1
                start = start.next
            left = 0
            middle = length // 2
            while head:
                if left == middle:
                    return head
                else:
                    left += 1
                    head = head.next
            return None
        
        firstHalf = midElement(head)
        secondHalf = firstHalf.next #initialize
        firstHalf.next = None #assigning pointers
        secondHalf = reverseList(secondHalf)
        firstPointer = head
        secondPointer = secondHalf
        while firstPointer and secondPointer:
            firstNext = firstPointer.next
            firstPointer.next = secondPointer
            secondNext = secondPointer.next
            secondPointer.next = firstNext
            firstPointer = firstNext
            secondPointer = secondNext
        return head
    #TC: O(n) SC: O(1)
            
            
            