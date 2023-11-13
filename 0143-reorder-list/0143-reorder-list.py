# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head or not head.next:
            return None

        # Step 1: Find the middle of the linked list
        slow, fast = head, head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        # # Step 2: Reverse the second half of the linked list
        # prev, curr = None, slow.next #4
        # slow.next = None #the first of the list is being broken from the other part of the list
        # while curr:
        #     curr.next = prev #4.next = null
        #     prev = curr #none = 4 move to the right
        #     curr = curr.next #curr becomes 5 and repeat this process
        # Step 2: Reverse the second half of the linked list
        prev, curr = None, slow.next
        slow.next = None
        while curr:
            next_temp = curr.next  # Save the next node
            curr.next = prev       # Reverse the current node's pointer
            prev = curr            # Move prev to the current node
            curr = next_temp       # Move to the next node


        # Step 3: Merge the two halves
        first, second = head, prev
        while second:
            temp1, temp2 = first.next, second.next
            first.next = second
            second.next = temp1
            first, second = temp1, temp2
        