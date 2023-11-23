class OrderedStream:

    def __init__(self, n: int):
        self.streamMap = {}
        self.pointer = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        res = []
        
        self.streamMap[idKey] = value
        
        while self.pointer in self.streamMap:
            res.append(self.streamMap[self.pointer])
            self.pointer += 1
        
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)