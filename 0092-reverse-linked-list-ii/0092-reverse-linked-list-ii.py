# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseBetween(self, head, left, right):
        """
        :type head: ListNode
        :type left: int
        :type right: int
        :rtype: ListNode
        Process:
            1. Edge cases:
                        No node found or left == right: return head
            2. Create a dummy node and dummy's next node
            3. Create pointers to find the left value
            4. The only changes need to be made are b/w left and right
                        a) hold the left in a temp variable
                        b) replace the hold by referencing it's next node before breaking the                              connection [pointer's next ----> temp's next]
                        c) find the temp's next pointer
                        d) the connection created in step b assign a pointer for that
        #TC: O(n) for number of nodes  SC: O(1) no aditional space + in-place reversal
        """
        
        if not head or left == right:
            return head
        pointer = prev = ListNode(None)
        prev.next = head
        for i in range(left - 1):
            pointer = pointer.next
        leftFound = pointer.next
        
        for i in range(right - left):
            #a
            hold = pointer.next #initialize/giving it a name
            #b
            pointer.next = leftFound.next
            #c
            leftFound.next = leftFound.next.next
            #d
            pointer.next.next = hold
        return prev.next
            
        
        