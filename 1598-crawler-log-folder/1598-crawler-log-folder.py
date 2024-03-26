class Solution:
    def minOperations(self, logs: List[str]) -> int:
        # Create a stack
        stack = []

        # Add/Remove items from stack
        for log in logs:
            if log == "../":
                if stack:
                    stack.pop()
            elif log == "./":
                continue
            else:
                stack.append(log)

        # Return the size of stack
        return len(stack)