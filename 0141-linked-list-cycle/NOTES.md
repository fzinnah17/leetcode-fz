1. Identify the problem: problem statement indicating the presence of a cycle
2. Initialize the pointers:
a. fast = head,
b. slow = head
3. Choose a movement strategy:
a. Tortoise and Hare: The fast pointer (the hare) moves faster than the slow pointer (the turtle).
fast = fast.next.next
slow = slow.next
4. Use while loops:
a. To move the pointers until you reach the end of the data structure or when you find a cycle.
while fast is not None and fast.next is not None:
5. Find cycles or repeating parts: This could happen when the fast pointer catches up to the slow pointer or when they both end up at the same element.
if fast == slow:
6. Handle edge cases: linked list or array that is empty or a structure that doesn't have any cycles.
if head is None:
return None
7. Time and space complexity: time complexity of O(N) and a space complexity of O(1)
​