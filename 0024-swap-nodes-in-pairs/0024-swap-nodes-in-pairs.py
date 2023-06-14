# Definition for singly-linked list. 
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        1. We already defined the LinkedList Class
        2. Identify the Problem Constraints and Requirements:
                a. swap every two adjacent nodes
                b. The input consists of the head of the given list
                c. output format: return head.next of the list after swapping the nodes
        3. Initialize Pointers and Variables:
                a. dummy
                b. current: to traverse the given list
                c. Starting with a dummy node and initializing it with the 'current' variable simplifies the logic. It serves as the starting point of the list.
        4. Handle Edge Cases: if not head: return None
        5. Traverse the Linked List: using a while loop. 
        6. Manipulate Pointers and Nodes: HOW DO I DO IT??????? 
        7. Keep Track of Relevant Information
        """
        dummy = ListNode(0)
        dummy.next = head
        current = dummy
        
        if not head:
            return None
        
        while current.next and current.next.next: #at least two nodes should be there to swap nodes
            firstNode = current.next
            secondNode = current.next.next
            nextNode = secondNode.next
            
            firstNode.next = nextNode
            secondNode.next = firstNode
            current.next = secondNode
            
            current = current.next.next #To make sure 'current' eventually points to the last node 'None'
        return dummy.next
    #TC: O(n) SC: O(1)
            
            
        