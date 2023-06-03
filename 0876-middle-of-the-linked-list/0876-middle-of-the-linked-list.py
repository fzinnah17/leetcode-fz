# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        """
        I can use the tortoise and hare method here.
        The slow pointer goes one step
        The fast pointer goes two steps
        while checking the 'if' conditions:
            if fast.next.next doesn't exist, then return slow(middle node)
        TC: O(n) for n nodes. SC: O(1) no space used
        """
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow #if both the fast and fast.next doesn't exist
        