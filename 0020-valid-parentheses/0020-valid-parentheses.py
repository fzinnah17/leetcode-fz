class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        To solve this we traverse through each character of string which consists of sign {}()[] only. When an open parenthesis comes like {, [, (  we push it into the stack. And when the closing parenthesis comes like }, ], )  we compare it from the top of the stack. If the closing parenthesis matches with the top of stack then we pop the character from the stack otherwise we return false.
        """
        from collections import deque
        stack = deque()
        
        for c in s:
            if c == "(" or c == "{" or c == "[":
                stack.append(c)
            elif len(stack): #it means something is in the stack so I can check for closing parentheses
                el = stack.pop()
                if el == "(" and c != ")":
                    return False
                if el == "{" and c != "}":
                    return False
                if el == "[" and c != "]":
                    return False
            else:
                return False #if I am starting with closed parentheses
        if len(stack):
            return False
        return True
                
            
                
        