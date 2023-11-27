class DLL():
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        """
        hashmap key = key, value = node reference
        DLL uage of the order
        """
        self.cacheMap = {} #key= key, val = node
        self.head = DLL(0, 0)
        self.tail = DLL(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.capacity = capacity
        
    
    def removeNode(self, node):
        ''' head <> [] <> [node] <> [] <> tail '''
        prev, nxt = node.prev, node.next
        prev.next, nxt.prev = nxt, prev
        
        
    def addNode(self, node):
        ''' head <> [] <> [] <> [node] <> tail '''
        prev = self.tail.prev
        prev.next = node
        self.tail.prev = node
        node.next = self.tail
        node.prev = prev
        

    def get(self, key: int) -> int:
        if key in self.cacheMap:
            node = self.cacheMap[key]
            self.removeNode(node)
            self.addNode(node)
            return node.val
        return -1
        

    def put(self, key: int, value: int) -> None:
        """
        check hashmap
        -- find
        -- check the capactiy
        --- i) under the cap
        --- ii) exceed the cap
        
        cap 2
        head <> [] <> [] <> [] <> tail
            
            
        
        """
        if key in self.cacheMap:
            self.removeNode(self.cacheMap[key])
        self.cacheMap[key] = DLL(key, value)
        self.addNode(self.cacheMap[key])
        
        # check cap
            # if <: remove from head
        if len(self.cacheMap) > self.capacity:
            lru = self.head.next
            self.removeNode(lru)
            del self.cacheMap[lru.key]
            
            
            
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)