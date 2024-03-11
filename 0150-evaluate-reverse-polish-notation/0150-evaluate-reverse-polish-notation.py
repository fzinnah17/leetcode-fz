class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
    # 1) Create a Stack which will store the numbers.
        stack = []

        for token in tokens:
            if token not in "+-/*":
                stack.append(int(token))
                continue

            # 2) When you come across an operator, pop the top two elements from the stack.
            number_2 = stack.pop()
            number_1 = stack.pop()

            # 3) Create a switch case which will act based on the type of the operator.
            # 4) For each switch case, perform their operations on the two variables and push the result into the stack again.
            result = 0
            if token == "+":
                result = number_1 + number_2
            elif token == "-":
                result = number_1 - number_2
            elif token == "*":
                result = number_1 * number_2
            else:
                result = int(number_1 / number_2)

            stack.append(result)

        # 5) At the end of the traversal, the element at the top of the stack is the result.
        return stack.pop()
"""
1. Operand Tokens: When an operand token (a numeric value) is encountered, it is converted to an integer and pushed onto the stack.

2. Operator Tokens: When an operator token ("+", "-", "*", or "/") is encountered, the code finds the top two values from the stack (bottomVal and topVal).

3. Negative Numbers: Checks for a "-" sign at the beginning of a token and treats it as part of the numeric value.

4. Stack Operations: Uses a stack to store intermediate results and operands, ensuring that the calculations are performed in the correct order."""   
            
        