class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        """
        [0, 1, 1, 4, 2, 1, 1, 0, 0]
        
        """
        
        stack = []
        
        output = [0]*len(temperatures) #key = index of the temparatures, value = temperature
        
        stack.append((0, temperatures[0]))
        
        for i in range(1, len(temperatures)):
            curr = temperatures[i]
            
            while stack:
                idx = stack[-1][0]
                prev = stack[-1][1]
                
                if curr > prev:
                    output[idx] = i - idx
                    stack.pop()
                    
                else:
                    break
                    
            stack.append((i, temperatures[i]))
        return output