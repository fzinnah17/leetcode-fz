class Solution(object):
    def removeDuplicates(self, s, k):
        # initial approach:
        # Things to do:
        # 1. We can append all the string values inside stack 
        # 2. And as long as the stack is being inserted chars i think we can check few 
            # things:
        #         a. if the current inserted character is the same as the previous one so stack [-1].
        #         b. While we are adding it, we can count the number occurences and see if 
        #             those are same as k. if so, remove those chars and it's counts'.
        #As we are doing it let's make sure the pointer is in between the boundary with while loop.
        if not s:
            return s
        if k == 1:
            return ""
        stack = [] #(current_ch, count) #stack[-1][0] means current, stack[-1][1] = count
        pointer = 0

        while pointer < len(s):
            #let's check IF the stack already has value in it and if it is the same as the current value being inserted.
            if stack and stack[-1][0] == s[pointer]:
                stack[-1][1] += 1
                if stack[-1][1] == k:
                    stack.pop()
            else:
                stack.append([s[pointer], 1])
            pointer += 1 #DO NOT FORGET TO CHANGE THE POINTER
        answer = ""
        for i in range(len(stack)):
            currenCh, count = stack[i][0], stack[i][1]
            answer += count * currenCh
        return answer
    
    
    




