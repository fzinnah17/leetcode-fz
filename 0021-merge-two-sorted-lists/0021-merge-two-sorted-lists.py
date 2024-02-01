# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      """
      step 1:
        - have the logic down
        - have a null node/dummy node
        - create a reference pointer to hold that dummy node
        - while both lists exist, compare the value and add whichever is smaller
      step 2:
        - then think of edge cases
        - so what if one list is bigger than the other/the elements are still left
        - just add those to the end
      """
      
      head = ListNode(None)
      # print(head)
      tmp = head #having a reference to the null node I created
      # print(tmp)
      
      while l1 and l2:
        if l1.val <= l2.val:
          #have the null pointer to set to the next val
          tmp.next = l1
          #shift the pointers to the next one in each iteration
          l1 = l1.next
        else:
          tmp.next = l2
          l2 = l2.next
        #tmp pointer has to change as well for it to reach the end of the lists
        tmp = tmp.next
        
      if l1:
        tmp.next = l1
      # if l2:
      else:  
        tmp.next = l2
      return head.next