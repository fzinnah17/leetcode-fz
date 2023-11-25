class OrderedStream:

    def __init__(self, n: int):
        self.messagesMap = {}
        self.ptr = 1

    def insert(self, idKey: int, value: str) -> List[str]:
        res = []
        # if self.ptr not in self.messagesMap:
        self.messagesMap[idKey] = value
        while self.ptr in self.messagesMap:
            res.append(self.messagesMap[self.ptr])
            self.ptr += 1
        return res
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)