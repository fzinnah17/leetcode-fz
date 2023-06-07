# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        Start with an empty result list: to store the result of the addition.
        Traverse the linked lists: Keeping track of the current node in each list
        add the corresponding digits and the previous carry if there is any
        Handling the carry
        How do I consider the scenario where one linked list is longer than the other.
        """
        carry = 0
        dummy = prev = ListNode(None)
        
        while l1 or l2 or carry:
            if l1:
                val1 = l1.val
            else:
                val1 = 0
            if l2:
                val2 = l2.val
            else:
                val2 = 0
            total = val1 + val2 + carry
            modNum = total % 10
            carry = total // 10
            
            prev.next = ListNode(modNum)
            
            prev = prev.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
        return dummy.next
    #TC: O(m + n), m is the size of l1 and n is the size of l2
    #SC: O(1) for no space used
                
        
        