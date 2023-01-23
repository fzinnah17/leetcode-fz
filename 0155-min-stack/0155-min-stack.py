class MinStack(object):
    from collections import deque
    def __init__(self):
        self.stack = deque()
        self.minStack = deque()
        

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        if not self.minStack or val <= self.minStack[-1]:
            self.minStack.append(val)
        self.stack.append(val)

    def pop(self):
        """
        :rtype: None
        """
        if self.stack[-1] == self.minStack[-1]:
            self.minStack.pop()
        self.stack.pop()        

    def top(self):
        """
        :rtype: int
        """
        return self.stack[-1]        

    def getMin(self):
        """
        :rtype: int
        """
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()