class Solution:
    def dailyTemperatures(self, temps: List[int]) -> List[int]:
        # Create an array to store the result (initialized with zeros)
        output = [0] * len(temps)
        
        # Create a stack to store temperature indices
        stack = []
        
        stack.append((0, temps[0]))
        
        # Iterate through the temperatures starting from the second day
        for i in range(1, len(temps)):
            # Get the current temperature
            currTemp = temps[i]
            
            # Check if the stack is not empty
            while stack:
                # Get the previous temperature and its index from the top of the stack
                prevTemp = stack[-1][1]
                prevIndex = stack[-1][0]
                
                # Compare the current temperature with the previous temperature
                if currTemp > prevTemp:
                    # If the current temperature is higher, update the result
                    output[prevIndex] = i - prevIndex
                    stack.pop()  # Remove the previous index from the stack
                else:
                    # If the current temperature is not higher, break the loop
                    break
            
            # Add the current temperature's index to the stack
            stack.append((i, temps[i]))
        
        # Return the resulting array
        return output
