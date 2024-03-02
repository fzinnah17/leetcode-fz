# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      """
      Time: O(m + n)
      Space: O(m or n)
      """
      temp = ListNode(None) #this is where we start building the list
      curr = temp
      carry = 0 # need it to go to the next iteration of the loop
      while l1 or l2 or carry:
        num1 =l1.val if l1 else 0
        num2 = l2.val if l2 else 0
        
        total = num1 + num2 + carry
        digit = total % 10
        carry = total // 10
        
        curr.next = ListNode(digit)
        curr = curr.next #current can move on
        
        #we can move to our next loop now
        #for different lengths of the lists use if statement
        if l1: l1 = l1.next
        if l2: l2 = l2.next
      return temp.next
        