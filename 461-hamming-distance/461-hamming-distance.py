class Solution(object):
    def hammingDistance(self, x, y):
        
        x = format(x, '0b')
        y = format(y, '0b')
        print (x, y)
        #('0b'0'0'1', '0b100')
        #    P
        
        #loop over the short one instead of long one
        short = max(len(x),len(y))
        # c= b.zfill(8)  
        x = x.zfill(short)
        
        y = y.zfill(short)
        count = 0
        
        for valOne, valTwo in zip(x,y):
            if valOne is not valTwo:
                count += 1
        # for index in range(len(x)): #index is working as one pointer
        #     if x[index] != y[index]:
        #         count += 1
            
        return count
                

        #(0 1 1 1)
        #       L
        #(0 0 0 0)
        # 
        #UMPIRE
        #1 (0 0 0 1)
        #         L position one, hamming distance = 2
        #2 (0 0 1 0)
        #         R position two position= two-one
        
        #1. convert to binary
        #2. having two pointers, both will check if the index values are different, if so then hamming dist goes up.
        #3. something to keep record the hamming distance (output)
        
        
        
        
        
        
        
        
        