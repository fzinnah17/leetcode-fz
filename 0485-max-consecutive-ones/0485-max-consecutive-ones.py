class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        Concept: keep track of the max length found so far. Return the longest window of 1's
        when traversing the array if 1 is found then length += 1
        but if 0 is found then call the max function
        Pseudocode:
        1. variables: length of the ongoing window, returned answer
        2. Loop through the array
            a. if '1' is found, then increase the length by 1
            b. if '0' is found, then find the maximum length of the window we got
                i. reset the length back to 0
        3. After the loop ends, we check what was the highest length we encountered
        4. Return that as the answer
        I have to pay attention that we are doing everything chronologically here
        """
        length = 0
        ans = 0
        for i in range(len(nums)):
            if nums[i] == 1:
                length += 1
            else:
                ans = max(ans, length)
                length = 0
        ans = max(ans, length)
        return ans
    #TC: O(n) SC: O(1)
            
                
        
        
        