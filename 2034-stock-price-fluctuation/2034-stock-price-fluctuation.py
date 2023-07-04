class StockPrice(object):
    """
    record of the stock -> 1. timestamp 2: price
    record is unordered/unsorted
    price can be corrected(hashMap?)
    """

    def __init__(self):
        self.currTime = 0
        self.hashMap = {}
        self.minHeap = []
        self.maxHeap = []

    def update(self, timestamp, price):
        """
Updates the price of the stock at a particular timestamp, correcting the price from any previous records at the timestamp.
    minheap is default heap implementation in python
    maxheap = minheap with negative values
    TC: O(logK)
                because inserting in heap = logK where k = elements in heap -----> 2*logk
        """
        self.hashMap[timestamp] = price
        heapq.heappush(self.minHeap, (price,timestamp))
        heapq.heappush(self.maxHeap, (-price,timestamp))
        self.currTime = max(self.currTime, timestamp)

    def current(self):
        """
Finds the latest price of the stock based on the current records.
    TC: Lookup -> O(1)
        """
        return self.hashMap[self.currTime]

    def maximum(self):
        """
Finds the maximum price the stock has been based on the current records.
    TC: O(Klogk) WHERE k = total elements in heap
        """
        currPrice, timestamp = heapq.heappop(self.maxHeap)
        while -currPrice != self.hashMap[timestamp]:
            currPrice, timestamp = heapq.heappop(self.maxHeap)
        heapq.heappush(self.maxHeap, (currPrice,timestamp))
        return -currPrice        

    def minimum(self):
        """
Finds the minimum price the stock has been based on the current records.
    TC: O(Klogk) WHERE k = total elements in heap
        """
        currPrice, timestamp = heapq.heappop(self.minHeap)
        while currPrice != self.hashMap[timestamp]:
            currPrice, timestamp = heapq.heappop(self.minHeap)
        heapq.heappush(self.minHeap, (currPrice,timestamp))
        return currPrice

# Your StockPrice object will be instantiated and called as such:
# obj = StockPrice()
# obj.update(timestamp,price)
# param_2 = obj.current()
# param_3 = obj.maximum()
# param_4 = obj.minimum()