class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def helper(k, piles): #number of hours Koko will need to eat all bananas at speed k
            total_hours = 0
            for pile in piles:
                if pile % k == 0: #goes through each pile, divides number of bananas by k aka middle
                    total_hours += (pile // k)
                else:
                    total_hours += ((pile // k) + 1)
            return total_hours
        left = 1
        right = max(piles)
        output = float("inf")
        
        while left <= right:
            middle = left + ((right - left) // 2)#middle is the spped/#of bananas
            minimum_ans = helper(middle, piles) 
            
            if minimum_ans <= h: #Koko can finish in time,this k (middle) is answer,we update output
                output = min(output, middle)
                right = middle - 1
            else:
                left = middle + 1 #we increase left to middle + 1 to explore higher speeds.
        return output
    """
    1. data is sorted, we have a monotonic function, and a defined range.
    2. if Koko can finish all bananas in h hours at speed k, she can also do so for any speed greater than k. This property of increasing feasibility (monotonicity)
    3. binary search is used for searching in sorted arrays, its real power lies in efficiently finding an answer in a sorted or monotonic decision space
    4. find the minimum k in a monotonic function (feasibility of finishing the bananas increases as k increases
    """