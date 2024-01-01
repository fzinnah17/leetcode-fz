class TimeMap:

    def __init__(self):
        """
        Hash table for keys to map to val and time (tuple)"""
        self.kvMap = {}
        
    def set(self, key: str, value: str, timestamp: int) -> None:
        """
        Make the hashmap
        if no value then add it to the map
        otherwise append"""
        if key not in self.kvMap:
            self.kvMap[key] = [(value, timestamp)]
        else:
            self.kvMap[key].append((value,timestamp))
        # print(self.kvMap)
    def get(self, key: str, timestamp: int) -> str:
        """
        Use binary search pointing to the timestamp and do the usual operations
        {
        foo : [(bar, 1), (bar2, 4)]
        }
        l = 0, r = len(map) - 1 for timestamps
        while l <= r: 
        mid
        if timestamp == pointerTime: return that pointerTime
        if < then move l = m + 1
        if > then move r = m - 1
        """
        # print(self.kvMap.values()) 
        if key not in self.kvMap:
            return ""
        l, r = 0, len(self.kvMap[key]) - 1
        res = ""
        
        while l <= r:
            m = l + ((r - l) // 2)
            # value, midTime = self.kvMap[key][m]
            # print(f"Key: {key}, Value: {value}, Timestamp: {midTime}")
            midTime = self.kvMap[key][m][1]
            # print(f"self.kvMap[key]: {self.kvMap[key]}")
            # print(f"midTime: {midTime}")
            # print(f"l: {l}, r: {r}")
            
            if midTime == timestamp:
                return self.kvMap[key][m][0]
            elif midTime < timestamp:
                res = self.kvMap[key][m][0] #closest match
                l = m + 1
            else:
                r = m - 1
        return res
                


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)