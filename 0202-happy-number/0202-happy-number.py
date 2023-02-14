class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        def nextNum(num):
            total = 0
            while num > 0:
                digit = num % 10
                total += digit * digit
                num //= 10
            return total
        slow, fast = n, n
    
        while True:
            slow = nextNum(slow)
            fast = nextNum(nextNum(fast))
            if slow == fast:
                break
        return slow == 1
        
        
            