class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Heapify the num array, create new array with negative values for each num, because python only supports minimum heaps.
        heap = [-num for num in nums]
        heapq.heapify(heap)

        # Remove k items from heap
        for _ in range(1,k):
            heapq.heappop(heap)
        
        # Return the top of the heap.
        return neg(heap[0])