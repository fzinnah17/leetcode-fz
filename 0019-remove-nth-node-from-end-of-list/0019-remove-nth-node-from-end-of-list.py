# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Create a dummy node to handle edge cases like removing the first node
        dummy = ListNode(0)
        dummy.next = head

        # First pass: find the length of the list
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        # Calculate the position from the start (length - n)
        length -= n

        # Second pass: reach the node just before the target
        temp = dummy
        while length > 0:
            length -= 1
            temp = temp.next

        # Remove the nth node from end
        temp.next = temp.next.next

        return dummy.next
