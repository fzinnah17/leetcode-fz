class Solution(object):
    def isHappy(self, n):
        """
        1. Identify the problem: problem statement indicating the presence of a cycle
        2. Handle edge cases:  that doesn't have any cycles.
                if head is None:
                    return None
        3. Initialize the pointers:
                a. fast = head,
                b. slow = head
        4. Use while loops with the given problem condition:
            a. To move the pointers until you reach the end of the data structure or when you find a cycle.
        while fast and fast.next:
        5. Choose a movement strategy:
            a. Tortoise and Hare: The fast pointer (the hare) moves faster than the slow pointer (the turtle).
        fast = fast.next.next
        slow = slow.next
        6. Find cycles or repeating parts: This could happen when the fast pointer catches up to the slow pointer or when they both end up at the same element.
        if fast == slow:
        7. Time and space complexity: time complexity of O(N) and a space complexity of O(1) 
               PSEUDOCODE:
        1. Take the modulo of the number -> then square it
        2. Take the quotient of the number -> then square it
        3. Add the numbers
        RECURSIVE PROCESS ABOVE
        check at any given point, if the value is 1, then return True
        otherwise return false
        """
        slow = fast = n
        def helper(digit):
            sumDigit = 0
            while digit > 0:
                moduloDigit = digit % 10
                digit = digit // 10 #the digit is changing as this number will be modulo for itself in it's next iteration. This is done so that even if we have 2^31 digits we can keep on going with the helper function by adding each digit's square till it's number '1'
                sumDigit += (moduloDigit**2)
            return sumDigit
        while True:
            slow = helper(slow)
            fast = helper(helper(fast))
            if fast == slow:
                break
        if slow == 1:
            return True
        return False
    """
    The time complexity of the solution is O(N), where N is the number of digits in the input number n. This is because in the worst case, the algorithm will iterate through all the digits of n until it either reaches 1 or enters a cycle.

The space complexity is O(1) because the algorithm does not use any additional data structures that grow with the input size. It only uses a constant amount of memory to store the variables slow and fast.

"""
            
            
        
        