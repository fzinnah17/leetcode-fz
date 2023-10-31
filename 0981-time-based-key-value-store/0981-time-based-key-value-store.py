class TimeMap: #object/result = TimeMap

    def __init__(self):
        self.dict = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        #more of like a hashmap key :value value: key
        if key not in self.dict:
            self.dict[key] = []
        self.dict[key].append([timestamp,value])
        
    def get(self, key: str, timestamp: int) -> str:
        #assumes that set was already called
        #previous time <= current time
        #multiple vales -> return largest previous time aka recent
        #no value match ->  ""
        if key not in self.dict:
            return ""
        time_array = self.dict[key]
        
        left = 0
        right = len(time_array) - 1
        
        while left <= right:
            middle = left + ((right - left) // 2)
            
            if time_array[middle][0] == timestamp:
                return time_array[middle][1]
            elif time_array[middle][0] < timestamp:
                left = middle + 1
            else:
                right = middle - 1
        if right < 0 or time_array[right][0] > timestamp:
            return ""
        return time_array[right][1]        
        
        
        


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)