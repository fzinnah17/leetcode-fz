# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        1. Identify the problem: problem statement indicating the presence of a cycle
        2. Handle edge cases: linked list or array that is empty or a structure that doesn't have any cycles.
        if head is None:
            return None
        3. Initialize the pointers:
                a. fast = head,
                b. slow = head
        4. Use while loops with the given problem condition:
            a. To move the pointers until you reach the end of the data structure or when you find a cycle.
        while fast and fast.next:
        5. Choose a movement strategy:
            a. Tortoise and Hare: The fast pointer (the hare) moves faster than the slow pointer (the turtle).
        fast = fast.next.next
        slow = slow.next
        6. Find cycles or repeating parts: This could happen when the fast pointer catches up to the slow pointer or when they both end up at the same element.
        if fast == slow:
        7. Time and space complexity: time complexity of O(N) and a space complexity of O(1)   
                """
        slow = fast = head

        if not head or not head.next:
            return None
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
            
        pointer = head
        while pointer != fast:
            pointer = pointer.next
            fast = fast.next
        return pointer
                
                
                
                
            
            
        
        
        