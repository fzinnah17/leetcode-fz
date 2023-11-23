class OrderedStream:

    def __init__(self, n: int):
        self.seen = {} # to store messages
        self.pointer = 1 #we will initially assume that the first message we will receive is from person 1
        

    def insert(self, idKey: int, value: str) -> List[str]:
        result = [] #we will eaither return empty or with string depending on the messages arrived
        self.seen[idKey] = value #the first message arrived is from person 3
        while self.pointer in self.seen:
            #nothing inside will run for the first message not being from person 1 as it's not found in the dictionary
            result.append(self.seen[self.pointer])
            #our pointer is still in 1st person and we found the first person's message so we will return that message inside the []
            self.pointer += 1
            
        return result #for the first message as we did not find person 1's message we will return empty []
        #1st loopseen = {3: "Person 3 Message"}
        


# Your OrderedStream object will be instantiated and called as such:
# obj = OrderedStream(n)
# param_1 = obj.insert(idKey,value)