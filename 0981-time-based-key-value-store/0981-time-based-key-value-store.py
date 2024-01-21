class TimeMap:
    """
    same key : [val1 : time stamp 1, val 2: timestamp 2, val 3: timestamp 3, .., .., ...]
    """

    def __init__(self):
        self.kvMap = {}

    def set(self, key: str, v: str, t: int) -> None:
        if key not in self.kvMap:
            self.kvMap[key] = [(v, t)]
        else:
            self.kvMap[key].append((v, t))
        # print(self.kvMap)
        # {
        # 'apple': [('red', 1), ('green', 4)], 
        # 'banana': [('yellow', 2)], 
        # 'orange': [('orange', 5)]
        # }
        
    def get(self, key: str, t: int) -> str:
        if key not in self.kvMap:
            return ""
        values = self.kvMap[key]
        # print(values)
        l, r = 0, len(values) - 1
        res = "" # timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev
        while l <= r:
            m = l + ((r - l) // 2)
            midTime = self.kvMap[key][m][1]
            
            if midTime == t:
                return self.kvMap[key][m][0]
            elif midTime < t:
                # timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the largest timestamp_prev
                res = self.kvMap[key][m][0]
                l = m + 1
            else:
                r = m - 1
                                 
        return res
            

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)