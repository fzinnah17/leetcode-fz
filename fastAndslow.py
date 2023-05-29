Fast & Slow Pointer Pattern Notes

1. Identify the problem: 
Look for hints in the problem statement indicating the presence of a cycle or the need to identify repeating elements. This pattern is especially useful in problems involving linked lists, arrays, or cycled sequences.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


2. Initialize the pointers: 
Start by setting both the fast and slow pointers to the head (or start) of the linked list or the first element of the array.
    fast = head
    slow = head


3. Choose a movement strategy: 
Find out how each pointer will move through the data structure. The fast pointer usually moves faster than the slow pointer moving two steps at a time instead of one. The requirements and constraints of the problem tell us exactly how to move.


4. Tortoise and Hare: Think of the fast pointer and the slow pointer as a tortoise and a hare. The fast pointer (the hare) moves faster than the slow pointer (the turtle). This comparison can help you get the idea and remember it.
    fast = fast.next.next
    slow = slow.next


5. Use while loops: 
In the Fast & Slow Pointers Pattern, while loops are often used because they give you more control over the iteration. Use while loops when you want to move the pointers until a certain condition is met, like when you reach the end of the data structure or when you find a cycle.
    while fast is not None and fast.next is not None:


6. Use the pointers to iterate: 
Move the pointers through the data structure using a loop or an iterative structure based on how they move(slow or fast). Iterate until a condition is met or one of the pointers reaches the end of the linked list or array.
    while fast != slow:


7. Find cycles or repeating parts: 
Keep track of comparisons or conditions that show that a cycle or repeating parts are present. This could happen when the fast pointer catches up to the slow pointer or when they both end up at the same element.
    if fast == slow:


8. Meeting point in a cycle: 
If the problem is to find where two pointers meet in a cycle, keep one pointer where it is and move the other pointer back to the beginning of the linked list or the first element of the array. Then, move both pointers at the same speed until they meet. This is their meeting point.
    slow = head
    while slow != fast:
        slow = slow.next
        fast = fast.next


9. Solve the problem: 
After detecting a cycle or repeating elements, use the pointers to solve the specific problem at hand. For example, if you need to find the beginning of a cycle in a linked list, you can reset one of the pointers and move them at the same pace until they meet again, indicating the beginning of the cycle.
    return slow


10. Handle edge cases: 
Think about edge cases, such as a linked list or array that is empty or a structure that doesn't have any cycles. Make sure that your implementation handles these situations effectively and gives the right result.
    if head is None:
        return None


11. Analyze the time and space complexity: 
Once you've solved the problem, you should look at the time and space complexity of your solution to make sure it meets the requirements and constraints of the problem.

The Fast & Slow Pointers Pattern often gives an efficient solution with a time complexity of O(N) and a space complexity of O(1), where N is the number of elements in the linked list or array.


12. Use hash sets to find cycles: 
You may need to find cycles in a linked list or an array at times. If you use a hash set to keep track of visited nodes, you can quickly find cycles by checking to see if a node has been visited before. When working with larger data structures, this can be very helpful.
    visited = set()
