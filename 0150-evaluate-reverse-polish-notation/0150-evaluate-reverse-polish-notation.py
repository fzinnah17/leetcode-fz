class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        res = 0
        stack = []
        
        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            else:
                topVal = stack.pop()
                bottomVal = stack.pop()
                if i == "+":
                    res = bottomVal + topVal
                elif i == "-":
                    res = bottomVal - topVal
                elif i == "*":
                    res = bottomVal * topVal
                else:
                    res = int(bottomVal / topVal)
                stack.append(res)
        return stack[0]
"""
1. Operand Tokens: When an operand token (a numeric value) is encountered, it is converted to an integer and pushed onto the stack.

2. Operator Tokens: When an operator token ("+", "-", "*", or "/") is encountered, the code finds the top two values from the stack (bottomVal and topVal).

3. Negative Numbers: Checks for a "-" sign at the beginning of a token and treats it as part of the numeric value.

4. Stack Operations: Uses a stack to store intermediate results and operands, ensuring that the calculations are performed in the correct order."""   
            
        