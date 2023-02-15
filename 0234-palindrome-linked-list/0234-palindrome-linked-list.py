# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
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
            fast = head
            slow = head
            while fast.next and fast.next.next:
                fast = fast.next.next
                slow = slow.next
            return slow
            # length = 0
            # start = head
            # while start:
            #     length += 1
            #     start = start.next
            # left = 0
            # middle = length // 2
            # while head:
            #     if left == middle:
            #         return head
            #     else:
            #         left += 1
            #         head = head.next
            # return None
        
        firstHalf = midElement(head)
        secondHalf = reverseList(firstHalf.next)
        result = True
        firstPointer = head
        secondPointer = secondHalf
        while result and secondPointer != None :
            if firstPointer.val != secondPointer.val:
                result = False
            firstPointer = firstPointer.next
            secondPointer = secondPointer.next
        firstHalf.next = reverseList(secondHalf)
        return result
        
            
        