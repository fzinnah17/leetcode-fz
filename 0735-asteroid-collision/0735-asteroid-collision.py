class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        Understand:
        positive test case: asteroids = [5,10,-5], Output: [5,10]
        negative test case: 
        a. input = [] output = []
        b. none of the asteroids collide: input = [1,2,3,4] output = [1,2,3,4]
        c. all of the asteroids collide: input = [1,-1,2,-2] output = []
        edge cases:
        a. input = [1] output = [1]
        b. input = [1,2] output = [1,2]
        c. input = [1,-1] output = []
        
        Match: Two pointers technique, one for iterating through the asteroids from left to right and another for storing the resulting asteroids after collision.
        Plan/pseudocode:
        1. Initialize the left pointer to 0.
        2. Iterate while left is less than len(asteroids) - 1 (since we don't need to compare the last element with the next one).
        3. Get the current asteroid value as curr and the next asteroid value as nxt.
            A. IF curr and nxt have:
                        i. the same direction (both positive)
                        ii. the same direction (both negative) or 
                        ii. if curr is negative and nxt is positive. If true, move to the next iteration by incrementing left.
            B. ELSE: (there is a collision between curr and nxt):
                        i. Check if their abs values are equal. if (abs(curr) == abs(nxt))
                                Remove both asteroids by popping the elements at left + 1 and left.
                        ii. If the abs value of curr is greater than nxt, if (abs(curr) > abs(nxt))
                                Remove the next asteroid by popping the element at left + 1.
                        iii. If the abs value of curr is smaller than nxt, if (abs(curr) < abs(nxt)),
                                Remove the current asteroid by popping the element at left.
            C. Set left to 0 to restart the iteration from the beginning. If we don't reset left to 0, the iteration will continue from its current position, which means it will skip some elements that may need to be reevaluated after a collision. This can lead to missing additional collisions and incorrect results.
        4. Return the updated asteroids list after all the collisions have been resolved.                       TC: O(n) SC: O(1)
        """
        left = 0        
        while left < len(asteroids) - 1: #not left <right what if there is no collisions at all
            curr = asteroids[left]
            nxt = asteroids[left+1]
            if (
                (curr < 0 and nxt < 0) or 
                (curr >= 0 and nxt >= 0) or 
                (curr < 0 and nxt >= 0)
            ):
                left += 1
            else:
                if (abs(curr) == abs(nxt)):
                    asteroids.pop(left + 1)
                    asteroids.pop(left)
                elif (abs(curr) > abs(nxt)):
                    asteroids.pop(left + 1)
                else:
                    asteroids.pop(left)
                left = 0
        return asteroids