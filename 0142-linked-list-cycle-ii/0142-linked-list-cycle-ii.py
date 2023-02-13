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
                current = slow
                while True:
                    current = current.next
                    cycleLength += 1
                    if current == slow:
                        break
                break #mandatory to break the loop
        if cycleLength > 0 and slow == fast:
            slow = head
            while fast != slow:
                slow = slow.next
                fast = fast.next
            return fast
        else:
            return 
        #TC: finding the cycle in a LinkedList with ‘N’ nodes: O(n)
        #.   finding the length of the cycle: O(n)
        #    find the start of the cycle: O(n) 
        #Therefore, the overall time complexity of our algorithm will be O(N).
        
        #SC: O(1)
                    
            
                        
        
        