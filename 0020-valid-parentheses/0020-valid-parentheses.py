class Solution:
    def isValid(self, s: str) -> bool:
        """
        Pseudocode:
        1. Edge case: odd length of the string: missing bracket -> False
        2. variables: 
            deque() for faster add/removal from both end, 
            hashmap to keep track of the brackets hashMap[key] = value {key : value} 
            key = )}] value = ({[
        3. for loop iterate over the string:
                a. if the closing bracket/key is found:
                        if stack exists:
                            remove the element
                        else:
                            dummy value
                            removed element != hashmap key(if not):
                                False
                b. add the parentheses
        4. if stack still exists with any brackets -> False
            else True
        TC: O(n) SC: O(n)                                                          
        """
        if len(s) % 2 != 0:
            return False
        stack = deque()
        #key = )}] value = ({[
        bracketMap = {')' : '(', '}' : '{', ']' : '['}
        for i in s:
            if i in bracketMap: #i is the closing parantheses for this condition, As you traverse the string s, you're more interested in checking if a closing bracket matches the last seen opening bracket (which would be on top of the stack).
                topBracket = stack.pop() if stack else '#'
                if bracketMap[i] != topBracket: 
                    return False
            else:
                stack.append(i)
        if len(stack):
            return False
        return True
                    