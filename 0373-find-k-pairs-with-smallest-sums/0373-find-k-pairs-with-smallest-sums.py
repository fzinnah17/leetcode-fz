class Solution(object):
    def kSmallestPairs(self, nums1, nums2, k):
        """The Time complexity of this algorithm is O(klogk) if k < n, because we repeat k times, and each time we do a O(logk) heappush.
        The Space complexity is O(n) in the worst case. This is because we use a min-heap called heap to store the pairs, and the heap can potentially hold all n pairs from nums1 and nums2. Additionally, we use the visited set to keep track of visited indices, which can store at most n unique pairs.
        """
        if not nums1 or not nums2:
            return []
        output = []
        heap = []
        visited = set()
        heappush(heap, (nums1[0] + nums2[0], 0, 0)) #create a heap, then push (heap,S0, Nidx1, Nidx2)
        visited.add((0,0))
        
        while len(output) < k and heap:
            val = heappop(heap) #Pop the root element (S0, N1,N2) out of the heap, add (Nidx1,Nidx2) to the result to be returned
            output.append((nums1[val[1]], nums2[val[2]]))
            #and immediately push (S1, Nidx1+1,N2idx) and (S2, N1idx, N2idx+1) into the heap, where S1 = nums1[Nidx1+1]+nums2[Nidx2], S2 = nums1[Nidx1] + nums2[Nidx2+1].
            if val[1] + 1 < len(nums1) and (val[1] + 1, val[2]) not in visited:
                heappush(heap, (nums1[val[1] + 1] + nums2[val[2]], val[1] + 1, val[2]))
                visited.add((val[1] + 1, val[2]))
            if val[2] + 1 < len(nums2) and (val[1], val[2] + 1) not in visited:
                heappush(heap,(nums1[val[1]] + nums2[val[2] + 1], val[1], val[2] + 1))
                visited.add((val[1], val[2] + 1))
        return output
    #https://leetcode.com/problems/find-k-pairs-with-smallest-sums/discuss/209985/python-heap-solution-with-detail-explanation
            
            
        
        """
        We can take advatage of the fact that the arrays are sorted
        Pseudocode:
        1. output = []
        2. We will have two pointers: one for nums1, another for nums2 using the nested for loops
        3. add the pair of numbers from each nums array till the lengths are reached
        4. append the pairs in the output list
        5. sort the output list according to their sum in ascending order
        6. traverse through the output list and find the k numbers

        output = []
        
        for up in range(len(nums1)):
            for bottom in range(len(nums2)):
                output.append([nums1[up], nums2[bottom]])
        output.sort(key=sum)
        output = output[:k] #How to get the first N elements of a list in Python? You can use the slicing operator [:N] , where N is the number of elements you want to retrieve from the beginning (index 0) of the given list
        The brute force approach to solving this problem is to compute the sum of all the pairs, sort the list of sums, and select the first 'k' elements from it. If the size of nums1 is m and size of nums2 is n, there will be m * n pairs in total that will be formed. As a result, it will take O(m⋅n) time to calculate the sum of all the pairs and O(m⋅n⋅log(m⋅n)) time to sort the list of sums. This will result in the time limit being exceeded (TLE) and memory limit being exceeded (MLE)."""
        