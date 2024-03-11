# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        # Create function to Reverse Linked List
        def reverseList(head: Optional[ListNode]) -> Optional[ListNode]:
            prev, curr = None, head
            while curr:
                next = curr.next
                curr.next = prev
                prev = curr
                curr = next
            
            return prev

        # Reverse Linked List
        r1 = reverseList(l1)
        r2 = reverseList(l2)
        
        # Add the two numbers in reverse
        currVal = 0
        carry = 0
        tempHead = ListNode()

        while r1 or r2:
            if r1:
                currVal += r1.val
                r1 = r1.next
            if r2:
                currVal += r2.val
                r2 = r2.next

            tempHead.val = currVal % 10
            carry = currVal // 10
            prevNode = ListNode(carry)
            prevNode.next = tempHead
            tempHead = prevNode
            currVal = carry
        
        return tempHead.next if carry == 0 else tempHead