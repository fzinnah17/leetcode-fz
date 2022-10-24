class Solution(object):
    def decodeString(self, s):
        if not s:
            return "" # if s is empty then return just empty string
        
        characters = "" #this is to keep track of what characters are there in the string
        pointerOne = 0 
#idea: the pointer will move thru the string and look for the alphabet. If it finds an alphabet, then it will be added to the characters string. Then the pointer will move forward and check the next value of the string. We keep on going till the string is out of boundary.
        while s[pointerOne].isalpha():
            characters += s[pointerOne]
            pointerOne += 1
            if pointerOne == len(s):
                return characters
        
        digits = ""
        while s[pointerOne].isdigit():
            digits += s[pointerOne]
            pointerOne += 1
            
        pointerTwo = pointerOne + 1 #this is to prevent edge case that there is already a bracket appeared.
        numofBrackets = 1 
        
        while numofBrackets:
            pointerTwo += 1 #to check if there are anymore brackets
            numofBrackets = numofBrackets + (s[pointerTwo] == "[") - (s[pointerTwo] == "]")
        return characters + int(digits) * self.decodeString(s[pointerOne + 1: pointerTwo]) + self.decodeString(s[pointerTwo+ 1 :])
    #int(digits) .... is the decoded version of the encoded string repeated k time/given digits times
            
            
        
        
            
            
        
        
        
        
        
        
        #output = "" i have to join the characters in the string       
        #"3[a2[c]]"
        #if condition 
        
        # 3    [    a    2    [    b   c   d    ]    ]
        #      p1
        #                                            p2
        #           ch
        
        #char = [b,c,d] -> bcd
        #key : 0 -> p1 - 1 == 3 -> abcdbcd
        
        #output = "bcdbcd"  -> key*char 
        #value[ch] + output -> "a" + "bcdbcd" -> "abcdbcdabcdbcdabcdbcd"
        
        
        #p1 checks [      p2 checks if it's a     ]
        #if p2 == p1, p1 moves all the way to p2
        
        #after finding
        #find p1 = [
        #find p2 = ] 
        
        #find ch? p1 + 1     check if the next is ch or not? += 1 while p2 != ch 
        #occur p1 - 1
        
        #output = ""
#         output = ""
#         #looping through the string 
#         for index in range(len(s)-1):
#             #two pointers at index 0 (p1,p2)
#             pointerOne, pointerTwo = s[0]
#         #p1 looks for [ and if it finds it then it stays there
#             if s[index] == '[':
#                 pointerOne += 1
                
#         #p2 looks for ] and if it finds it then it stays there, but if p2 = [ it will be p1=p2, p1 pointer will move forward
#             if pointer
        #ch - > p1 + 1 and it will increment till it becomes p2 = ch
        #key : p1 - 1 
        #key * char and it will be joined inside output
        
        #p1 is decemented till it finds [, p2 increments till it finds ]
        #ch decements again to find p1+ 1
        #same thing with key -> join in output
        
        
        
        
        
        
        
        
        
        
        
        
        
        #p1 - 1 
        #retrive the character

        #string = "c*2"
        
        #then our pointer goes back till it finds [, adter finding then it goes to ]
        #ch == p1 initially, then move forward to find the first char
        
        