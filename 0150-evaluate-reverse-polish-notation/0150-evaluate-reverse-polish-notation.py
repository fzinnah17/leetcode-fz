from collections import deque
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = collections.deque()
        for i in tokens:
            if i in "+-*/":
                first = stack.pop()
                second = stack.pop()
                if i == "+":
                    stack.append(int(first) + int(second))
                elif i == "-":
                    stack.append(int(second) - int(first))
                elif i == "*":
                    stack.append(int(first) * int(second))
                elif i == "/":
                    stack.append(int(int(second) / float(first)))
            else:
                stack.append(int(i))
        return stack[-1]
            # if i = "+" or i = "-" or i = "*" or i = "/":
                
        
        