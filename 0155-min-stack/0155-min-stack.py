class MinStack:
    #deque() helps to have faster access to append and remove from both sides -> so faster TC
    """
    'auxiliary stack' concept. auxiliary: providing additional help and support.
    The main idea behind MinStack is to maintain an auxiliary stack, in this case, minStack, which keeps track of the minimum element seen so far. 
     This ensures that at any point, the top of the minStack represents the current minimum of the main stack/regular stack"""
    def __init__(self):
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        """push on the min stack only:
                a. if the minstack is empty
                b. if the value is less than the value that is already there on the top"""
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self) -> None:
        """min stack values can only be removed if the value is matching with the topmost value of the stack
        new element could potentially be the new minimum or might become the minimum if the current minimum is popped out.
        if the minimum element is removed from the main stack, it's no longer relevant to the minStack"""
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()

    def top(self) -> int:
        """only for the top of the regular stack"""
        return self.stack[-1]

    def getMin(self) -> int:
        """only for the top/recent minimum of the min stack
        contains the current minimum of the main stack."""
        return self.minStack[-1]
    
    """
    TC: O(1) for all operations because just pushing, popping, or retrieving the top element for both stacks. There are no iterations or loops.
    SC: O(n) where n is the number of elements in the main stack. In the worst case, all elements in the main stack could be in descending order, and hence the minStack would contain all these elements as well.
    It's essential first to update the minStack before the main stack. Why? Because the logic of the operation might depend on the current state of the main stack. For instance, in the pop operation, you need to compare the top of the main stack with the top of the minStack. If you pop the main stack first, you would lose that top element before making the comparison.
    Here, the essence is using an auxiliary stack to keep track of a property (in this case, the minimum value) of the main stack. This concept can extend to other properties, not just the minimum
    """


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()