class Solution:
    def mySqrt(self, x: int) -> int:
        l,r = 0, x
        # While left pointer is less than right pointer we have not exhausted the possible numbers
        while l <= r:
            # Get the mid point of the two pointers 
            mid = (l + r) // 2

            # Check if mid point is less than or greater than or equal to our target
            if mid ** 2 == x:
                # If mid point is equal to our target then return our mid point
                return mid
            
            elif mid ** 2 < x:
                # If mid point is less than our target, then we move the left pointer up to mid point + 1, because everything left of the mid point would be even further away from our target
                l = mid + 1
            else:
                # If mid point is greater than our target, then we move the right pointer down to mid point - 1, because everything to the right of mid point is invalid. 
                r = mid - 1
                
        # Return the right pointer for the closes number to square for our target as it is the last remaining valid number.
        return r
        