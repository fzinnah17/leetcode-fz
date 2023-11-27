class OrderedStream:

    def __init__(self, n: int):
        self.mMap ={}
        self.ptr = 1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        res = []
        self.mMap[idKey] = value
        
        while self.ptr in self.mMap:
            res.append(self.mMap[self.ptr])
            self.ptr += 1
        return res


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)