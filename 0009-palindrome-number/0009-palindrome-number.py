class Solution(object):
    def isPalindrome(self, x):
        # if x = 121 then it is read same from backwards, so we can return true
        # if x = 123, then it is not read same from backwards, so we return false
        
        #we can have two pointers
        #left = x[0]
        #right = len(x)-1
        #be careful it is not a string so convert it into a string
        if x < 0:
            return False
        x = str(x)
        leftPointer, rightPointer = 0, len(x) - 1
        
        #condition is while left < right: ;; if it is still in the bound, then
        #check if x[left] = x[right]
        
        while leftPointer <= rightPointer:
            if x[leftPointer] != x[rightPointer]:
                return False
            else:
                leftPointer += 1
                rightPointer -= 1 #if yes then left += 1, right -=1
        return True

            
        
            
        
        #if yes then left += 1
        #right -=1
        
        #if x[left] != x[right]:
        #break
        
        #we stop when left = right
        #but what do we do at left = right ? do we create another while loop inside?
        
        #another condition should be if all the numbers match in the bound, then we return #t
        
        #I think we have to check odd? and even?
        
        
        