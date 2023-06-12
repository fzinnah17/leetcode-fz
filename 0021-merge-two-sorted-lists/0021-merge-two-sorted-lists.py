# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        TC: O(N) SC: O(N)
        """
        temp = ListNode(0)
        current = temp #Initialize Pointers and Variables
        
        if not list1 and not list2:
            return None #Handle Edge Cases
        
        list1Ptr = list1 #Initialize Pointers and Variables
        list2Ptr = list2 
        
        while list1Ptr and list2Ptr: #Traverse the Linked List
            if list1Ptr.val < list2Ptr.val: #Manipulate Pointers and Nodes
                current.next = list1Ptr #Keep Track of Relevant Information(current connects to other list values and the position of it moves according to the conditional statements)
                list1Ptr = list1Ptr.next
            else:
                current.next = list2Ptr
                list2Ptr = list2Ptr.next #Implement the Solution Logic continues until one of the input lists is exhausted
            current = current.next
        if list1Ptr: #still has remaining nodes after the loop
            current.next = list1Ptr
        if list2Ptr:
            current.next = list2Ptr
        return temp.next
                   