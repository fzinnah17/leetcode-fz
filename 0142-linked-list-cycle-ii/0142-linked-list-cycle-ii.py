# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        slow, fast = head, head
        cycleLength = 0
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                cycleLength += 1
                break
        if cycleLength > 0 and slow == fast:
            slow = head
            while fast != slow:
                slow = slow.next
                fast = fast.next
            return fast
        else:
            return
                    
            
                        
        
        