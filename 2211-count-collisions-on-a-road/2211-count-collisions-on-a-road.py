class Solution(object):
    def countCollisions(self, directions):
        stack = [directions[0]]
        count = 0
        for i in range(1,len(directions)):
            if stack[-1] == 'R' and directions[i] == 'L':
                count += 2
                stack.pop()
                if len(stack) > 0:
                    while len(stack) > 0 and stack[-1] == 'R':
                        stack.pop()
                        count += 1
                stack.append('S')
            elif stack[-1] == 'R' and directions[i] == 'S':
                count += 1
                stack.pop()
                if len(stack) > 0:
                    while len(stack) > 0 and stack[-1] == 'R':
                        stack.pop()
                        count += 1
                stack.append('S')
            elif stack[-1] == 'S' and directions[i] == 'L':
                count += 1
                stack.append('S')
            else:
                stack.append(directions[i])
            i += 1
        return count
                
                
        
#1. if the car is moving R and the car next to it is moving L -> RL count += 2, append S
#2. if the car is moving R and the very next car is stationary -> RS count += 1, append S
#3. if the first car is S and the next car is moving left -> SL count += 1
#4. if two or more cars is moving in right/left direction and later on some collision take place and the car become stationary -> "LLRLRLLSLRLLSLSSSS" this test case fails count += 1


  
    
    
    