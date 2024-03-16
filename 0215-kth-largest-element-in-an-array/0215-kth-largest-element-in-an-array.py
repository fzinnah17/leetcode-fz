class Solution:
    #n >>>>>>>>>>> k, we are just only taking a look at the 5th largest number
    #T: O(nlogk), S: O(k) -> because heap is only size k
    
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #start with nothing, here time is O(1)
        heap = []
        #min heap in python
        heapq.heapify(heap) #T: O(1), S: O(1)
        
        #use heap as a buffer by pushing stuff into the heap only k items from the given item, 
        #so that if it exceeds then it will be popping from the top(which is on the right side). Then it will make sure that the top item is always the largest element.
        
        for i in range(len(nums)): #T: n * log(k)
            if i < k:
                heapq.heappush(heap, nums[i]) #T: logn
            elif nums[i] > heap[0]:
                #pop the top of the heap and push the number in
                heapq.heapreplace(heap, nums[i]) #same as popping then pushing, T: O(log2n)
        return heap[0]