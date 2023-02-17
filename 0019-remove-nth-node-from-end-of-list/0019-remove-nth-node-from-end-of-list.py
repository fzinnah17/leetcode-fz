# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        1. Create a dummy head to prevent edge cases
                what's dummy next?
        2. Create two pointers that is pointing to dummy
        3. The fast pointer should move n nodes ahead so use for loop
        4. Our loop breaks with fast having no value, so keep on looping till fast and fast's next value has value in it
                as we are looping,
                    a. slow moves one step
                    b. so as well fast
        5. delete the slow's next node by referencing slow's next pointer to be pointing to fast
        6. return the list
        """
        
        dummy = ListNode(None)
        dummy.next = head
        slow, fast = dummy,dummy
        
        for i in range(n):
            fast = fast.next
            
        while fast and fast.next:
            slow = slow.next
            fast = fast.next
        slow.next = slow.next.next
        return dummy.next
    #TC: O(n) SC: O(1)
        