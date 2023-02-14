class Solution(object):
    def isHappy(self, n):
        def nextNum(n):
            total = 0
            while n > 0:
                remainder = n % 10
                total += remainder * remainder
                n //= 10
            return total
        
        slow, fast = n,n
        while True:
            slow = nextNum(slow)
            fast = nextNum(nextNum(fast))
            if slow == fast:
                break
        return slow == 1
        