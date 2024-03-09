# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        l, r = 1, n
        # While left pointer is less than right pointer we have not exhausted the versions
        while l < r:
            # Get the mid point of the two pointers
            mid = (l + r) // 2

            # Check if mid point is bad or not
            if isBadVersion(mid):
                # If mid point is bad then there might be more bad versions before it, shift right pointer and check for earlier bad version.
                r = mid
            else:
                # If mid point is good then we know that everything to the left is good, shift left pointer to check for bad version in right half
                l = mid + 1
        # Return the right pointer for first bad version
        return r