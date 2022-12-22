class Solution(object):
    def findMaxAverage(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: float
        1. Loop thru the array to take n = k elements
        2. Move the window and subtract the n out of the bound.
        3. Add the new n.
        4. Variable to keep track of max value
        5. Variable to keep track of current sum.
        """
        #current sum
        currSum = 0.0
        #my starting sum is 0
        startVal = 0
        #it is adding all the subarray values
        result = []
        
        #loop thru the array
        for i in range(len(nums)):
            #Every time current sum is being added with each element
            currSum += nums[i]
            #as long as the window exceeds k
            if i >= k - 1:
                #the result takes the average
                result.append(currSum/k)
                #remove the starting value
                currSum -= nums[startVal]
                #update the new start
                startVal += 1
        #all the average values are in the new array so will find the maximum of it
        return max(result)
    #TC: O(N), SC: O(N)
                
            
        
        