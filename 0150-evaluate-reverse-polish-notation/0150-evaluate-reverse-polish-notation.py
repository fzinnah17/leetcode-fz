class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        """
        we can keep on adding the integers to the stack
        as soon as we find a valid operator we take out the last two numbers, do that operation
        add that operation to the result that we will return"""
        
        stack = []
        res = 0

        for i in tokens:
            if i.lstrip('-').isdigit():
                stack.append(int(i))
            elif i in ["+", "-", "*", "/"]:
                lastNum = stack.pop()
                prevNum = stack.pop()
                if i == "+":
                    res = prevNum + lastNum
                elif i == "-":
                    res = prevNum - lastNum
                elif i == "*":
                    res = prevNum * lastNum
                elif i == "/":
                    res = int(prevNum / lastNum)
                stack.append(res)
        if stack:
            return int(stack[0])
                        