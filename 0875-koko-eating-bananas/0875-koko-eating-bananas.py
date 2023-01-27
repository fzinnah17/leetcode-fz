class Solution(object):
    def minEatingSpeed(self, piles, h):
        left, right = 1, max(piles)
        result = right
        while left <= right:
            hours = 0
            middle = left + ((right - left)//2)
            for i in range(len(piles)):
                hours += round(piles[i]//middle)
                #this is to round up the number to an upper value
                if piles[i] % middle != 0:
                    hours += 1 #done iterating
            if hours <= h:
                result = min(right, middle)
                right = middle - 1 
            if hours > h:
                left = middle + 1
        return result 
    
    # if elements[middle] < value:
    #     left = middle + 1
    # elif elements[middle] > value:
    #     right = middle - 1
                