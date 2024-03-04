# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        """
      Fred's way
      1. can n be larger than the linked list?
      2. is it singly or doubly linked list?
      3. will the loop have any cycle?
      4. does n start from 0 or 1? it's 1 bc it's from the end of the list
      
      - come up with testcases:
        [1,2,3], n = 1 return [1,2]
        [1,2,3,4], n = 4 return [2,3,4]
      
      - can we use multiple passes? temple head? two pointers?
        - multiple passes: first get length of the list, that's how we know the nth node from the end of the list
        - one pass: two pointer strategy can help us look ahead
        - temp head: we can point to the head
      """
        temp = ListNode()
        slow = temp
        slow.next = head
        
        #have another pointer at temp
        fast = temp
        
        for i in range(n):
            fast = fast.next
        
      #we don't know how many times so while loop
        while fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return temp.next
        