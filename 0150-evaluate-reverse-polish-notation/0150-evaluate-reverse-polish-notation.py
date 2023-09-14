class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        TC: O(n)
        SC: O(n)"""
        stack = deque()
        
        def helper(operator):
            return operator in ["+", "-", "*", "/"]
        
        for t in tokens:
            if helper(t):
                a = stack.pop()
                b = stack.pop()
                if t == "+":
                    stack.append(a + b)
                elif t == "-":
                    stack.append(b - a)
                elif t == "*":
                    stack.append(b * a)
                elif t == "/":
                    stack.append(int(b / a))
            else:
                stack.append(int(t))
        return stack[0]
                    
            
        