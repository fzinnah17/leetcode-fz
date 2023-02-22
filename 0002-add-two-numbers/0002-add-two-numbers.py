# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        1. Have two pointers
        2. if l1 and l2:
            Two pointers sum < 10   -----> add it in the linked list
            Two pointers sum > 10   -----> add the modulo of the addition (%) in the list
                            take the quotient of the number and add it with the next addition
        3. Edge case:
                    a. l1 length > l2 length then put the remaining l1 length in the output
                    b. l2 length > l1 length then put the remaining l2 length in the output
        TC: O(m+n) length of the nodes   SC: O(1) for no space used, BUT if we count the output as memory, then it is O(max(m,n)).
        """
        #.next after means change position
        carry = 0
        dummy = prev = ListNode(None)
        
        while l1 or l2 or carry:
            # if l1:
            #     digit1 = l1.val
            # else:
            #     digit1 = 0
            # if l2:
            #     digit2 = l2.val
            # else:
            #     digit2 = 0
            digit1 = l1.val if l1 else 0
            digit2 = l2.val if l2 else 0
            if l1 and l2:
                sumNodes = digit1 + digit2 + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                sumNodes = digit1 + carry
                l1 = l1.next if l1 else None
            else:
                sumNodes = digit2 + carry
                l2 = l2.next if l2 else None
            carry = sumNodes // 10 #quotient
            sumNodes = sumNodes % 10 #modulo
            prev.next = ListNode(sumNodes)
            prev = prev.next
            
        return dummy.next
                
                
            