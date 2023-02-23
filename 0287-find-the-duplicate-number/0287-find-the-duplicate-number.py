class Solution(object):
    def findDuplicate(self, nums):
        """Regarding the use of a dummy node with ListNode(None), this approach is specific to linked lists and is not applicable to this problem, as we are dealing with an array that simulates a linked list.
        We cannot use slow.next and fast.next.next to move the pointers in this problem, because we are not dealing with a linked list in the traditional sense. Instead, we are using the given array to simulate a linked list, where the value of each element in the array represents the index of the next element in the list.
        
        To implement this approach, we can use two pointers, a slow pointer and a fast pointer. We start by setting the slow pointer to the first node and the fast pointer to the second node. We then move the slow pointer one step at a time and the fast pointer two steps at a time until they meet. At this point, we know that there is a cycle in the linked list.
        We use two pointers: ptr1, which starts from the beginning of the array, and ptr2, which starts from the node where slow and fast pointers meet. We move both pointers one step at a time until they meet, which gives us the start of the cycle.
        TC: O(n) SC: O(1)
        """
        
        slow = nums[0]
        fast = nums[0]
        
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        pointer1 = nums[0]
        pointer2 = slow
        
        while pointer1 != pointer2:
            pointer1 = nums[pointer1]
            pointer2 = nums[pointer2]
        return pointer1
        
        
"""        #TC+ SC: O(n)
        hashSet = set()
        
        for i in nums:
            if i in hashSet:
                return i
            hashSet.add(i)
            """
"""SC: O(1)"""
        
        