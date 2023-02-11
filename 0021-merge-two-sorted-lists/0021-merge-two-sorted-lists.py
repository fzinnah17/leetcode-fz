# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        Brute force Approach: We can create a new empty list. Then, we can iterate over the first list and add it into the new empty list. Afterwards, we can follow the same approach with the second list. As the list is filled with both given list nodes, we can sort the new list. After sorting, we have to assign the pointers to create a new LinkedList. It means we are reconstructing a new linkedlist maintaining the order of the new array.
        #TC: O(L+M(Nlogn)) = L+M is the nodes from both lists. SC: O(N)
        This is inefficient because of three factors:
                1. We do not take use of the benefits of a linkedlist. LinkedLists are pretty flexible due to their pointers; if we know the references, we can move them in the array in constant time.
                2. We do not make advantage of the problem requirement. The requirement states clearly that L1 and L2 must be sorted independently. Sorting on a new array therefore ignores the fact that these lists are already sorted.
                3. In our case, we make use of additional space. A new array and linkedlist are formed to store the values from L1 and L2.
        """
        
        head = ListNode(None)
        start = head #I can not lose the reference of my root so need to hold it before everything
        while list1 and list2:
            if list1.val < list2.val:
                head.next = list1 #head is being initialized to the next value so .next is before
                list1 = list1.next #assigning so .next is coming later
            else:
                head.next = list2
                list2 = list2.next
            head = head.next
        if list1 != None and list2 == None:
            head.next = list1
        elif list1 == None and list2 != None:
            head.next = list2
        elif list1 == None and list2 == None:
            return None
        return start.next
    #TC: O(n) SC: O(1)
    
    
    
    
    
            