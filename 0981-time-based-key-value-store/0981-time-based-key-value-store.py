class TimeMap:

    def __init__(self):
        self.dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([value,timestamp]) 
    
    def get(self, key: str, timestamp: int) -> str:
        #think the timestamp as the target here
        res = ""
        if key not in self.dict:
            return ""
        value_list = self.dict[key]
        # print(value_list)
        # [['bar', 1]]
        # [['bar', 1]]
        # [['bar', 1], ['bar2', 4]]
        # [['bar', 1], ['bar2', 4]]
        left, right = 0, len(value_list) - 1
        
        while left <= right:
            middle = left + ((right - left) // 2)
            
            if value_list[middle][1] <= timestamp:
                res = value_list[middle][0] #update with the value
                left = middle + 1
            else:
                right = middle - 1
        return res
        

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)