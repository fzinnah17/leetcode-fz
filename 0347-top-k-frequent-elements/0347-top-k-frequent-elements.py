class Solution(object):
    def topKFrequent(self, nums, k):
        """
        Pseudocode:
        1. Count all the numbers of the array TC: O(n)
        2. Find the most common numbers based on the given parameter 'k' (value, #occurences) 
        TC: O(n) SC: O(n) as it is returning a list
        3. create an empty array to add the values to return later SC : O(n)
        4. For loop to go over the most common number list TC: O(n)
            a. append the first index of the tuples in that new array
        5. Return the result array
        
        TC: O(n) + O(n) + O(n): O(n) = O(n) 
        SC: O(n) + O(n) = O(n)
        """
        c = collections.Counter(nums)
        commonNum = c.most_common(k)
        # print(c.most_common(k)) [(1,3), (2,2)]
        result = []
        for i in commonNum:
            result.append(i[0])
        return result
            
        # return [i[0] for i in commonNum] list comprehension line
        