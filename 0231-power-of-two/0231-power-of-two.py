class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if(n==1):
            return True
        for i in range(0,n):
            power=pow(2,i)
            if(power<n):
                continue
            if(power==n):
                return True
            if(power>n):
                return False
        return False 