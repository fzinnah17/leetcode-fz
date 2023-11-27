class DLL:
    
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cacheMap = {}
        self.head = DLL(0, 0)
        self.tail = DLL(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head
        
    """
    head <> [] <> [node] <> [] <> tail
    """
    def removeNode(self, node):
        """give the variable names to the nodes"""
        prev, nxt = node.prev, node.next
        nxt.prev, prev.next = prev, nxt
        
    def addNode(self, node):
        """
        give the variable names to the nodes
                         prev
            head <> [] <> [] <> tail
            head <> [] <> [] <> [node] <> tail"""
        prev = self.tail.prev
        self.tail.prev = node
        prev.next = node
        node.next = self.tail
        node.prev = prev
        
        
    def get(self, key: int) -> int:
        if key in self.cacheMap:
            node = self.cacheMap[key]
            self.removeNode(node)
            self.addNode(node)
            nodeVal = node.val
            return nodeVal     
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.cacheMap:
            #update the value of the key -> remove the old one
            self.removeNode(self.cacheMap[key])
        #add the key-value pair to the cache if it doesn't exist or if we have to update
        self.cacheMap[key] = DLL(key, value)
        self.addNode(self.cacheMap[key])
        # If the number of keys exceeds the capacity from this operation
        if len(self.cacheMap) > self.cap:
            lru = self.head.next
            self.removeNode(lru)
            del self.cacheMap[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)