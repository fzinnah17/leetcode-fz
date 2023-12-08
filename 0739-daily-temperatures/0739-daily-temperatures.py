class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        """
        
        stack = [73, 74, 75, 71, 69, 72, 76 ]
        maxStack = [73, 74, 75]
        check if the next added temp to maxStack is greater or less than the current day temparature in the stack
        if greater than 1 day
        if not: count += 1
        output = [1, 1, 4, ]"""
        output = [0] * len(temps)
        stack = []
        stack.append((0, temps[0]))
        
        for i in range(1, len(temps)):
            currTemp = temps[i]
            # print("Current Temperature: ", temps[i])
            while stack:
                prevTemp = stack[-1][1]
                prevIndex = stack[-1][0]
                # print("Prev Temp & Index: ", stack[-1][1], "&", stack[-1][0])
                if currTemp > prevTemp:
                    # print("Stack: ", stack)
                    output[prevIndex] = i - prevIndex
                    stack.pop()
                    # print("i: ", i)
                    # print("i - prevIndex = ", i - prevIndex)
                    # print()
                else:
                    break
             
            stack.append((i, temps[i]))
        return output