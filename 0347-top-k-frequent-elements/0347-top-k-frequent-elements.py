from collections import defaultdict
from collections import Counter
class Solution(object):
    def topKFrequent(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        Brute Force: Iterate outer for loop k times and inner for loop n times to find the element that is most frequent and unique/not considered in any of the previous iterations
Time: O(nk)
Space: O(n) storing elements of nums with its frequency
Bucket sort is mainly useful when input is uniformly distributed over a range.
        """
        #[4,4,1,3,1,4,2,7]
        #[    1      2 3 4 5 6 7 8] #O(n) scanning
        #[[3][2][7]  1 4 x x x x x]  ----> Buckets #O(n) scanning : WE ARE READING FROM RIGHT TO LEFT
        #[[2,3,7]    1 4 x x x x x] 
        #       k = 5  <----- RETURNING [4,1,2,3,7],     k = 2 <---- RETURNING [4,1]
        #       k = 6 IS INVALID BECAUSE WE HAVE ONLY N NUMBERS < K  <------- #TC &SC: O(n)
        
        """Steps:
        1. I am creating a table {key:values}
            key: i(counts) ---> len(array)
            values: numbers ---> numbers from the array
        2. Insert the numbers
        3. Sort the numbers
        """    
        if k == len(nums):
            return nums
        #[4,4,1,3,1,4,2,7]
        #c = Counter(nums) #Counter({ 4: 3,    1: 2,    2: 1,    3: 1,    7: 1 }) unordered
        d = collections.defaultdict(int) 
                        #defaultdict(<type 'int'>, {1: 2,  2: 1,  3: 1,  4: 3,  7: 1}) ordered
        for i in nums:
            d[i] += 1 #ALTERNATIVE OF Counter
        f = defaultdict()          # defaultdict({1: [2, 3, 7], 2: [1], 3: [4]})
        for num, freq in d.items(): # O(n)
            if freq not in f:
                f[freq] = [num] 
            else:
                f[freq].append(num)
        res = []
        for i in range(len(nums),0,-1): # O(n)
            if i in f:
                res += f[i]
        return res[:k] #[4,1]
    
        
        
        #For testcase, [-1,-1] k = 1 
        #       d: defaultdict(<type 'int'>, {-1: 2}) 
        #       f: defaultdict(None, {2: [-1]})

        
        