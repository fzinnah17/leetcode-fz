class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head
        self.m = {}

    def addnode(self, newnode):
        temp = self.head.next
        newnode.next = temp
        newnode.prev = self.head
        self.head.next = newnode
        temp.prev = newnode

    def deletenode(self, delnode):
        delprev = delnode.prev
        delnext = delnode.next
        delprev.next = delnext
        delnext.prev = delprev

    def get(self, key: int) -> int:
        if key in self.m:
            resnode = self.m[key]
            res = resnode.val
            del self.m[key]
            self.deletenode(resnode)
            self.addnode(resnode)
            self.m[key] = self.head.next
            return res
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.m:
            existingnode = self.m[key]
            del self.m[key]
            self.deletenode(existingnode)
        if len(self.m) == self.cap:
            del self.m[self.tail.prev.key]
            self.deletenode(self.tail.prev)
        self.addnode(Node(key, value))
        self.m[key] = self.head.next

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)