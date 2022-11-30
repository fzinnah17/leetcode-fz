# class UndergroundSystem:

#     def __init__(self):
        

#     def checkIn(self, id: int, stationName: str, t: int) -> None:
        

#     def checkOut(self, id: int, stationName: str, t: int) -> None:
        

#     def getAverageTime(self, startStation: str, endStation: str) -> float:
        


# # Your UndergroundSystem object will be instantiated and called as such:
# # obj = UndergroundSystem()
# # obj.checkIn(id,stationName,t)
# # obj.checkOut(id,stationName,t)
# # param_3 = obj.getAverageTime(startStation,endStation)

class UndergroundSystem(object):
    '''Station1 - Station2 - Station3 '''
    """"""
    ''''''
    def __init__(self): #SC: O(n)
        self.startStation = {}
        self.total = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.startStation[id] = (stationName, t)  # T-O(1)
        return
    def checkOut(self, id: int, endStation: str, t: int) -> None:
        checkin_station, checkin_time = self.startStation[id]
        del self.startStation[id] #S-O(1)
        # (start_station, end_station) = [timeEnd - timeStart, toalJourney+1] 
        if (checkin_station, endStation) in self.total:
            self.total[(checkin_station, endStation)][0] += 1
            self.total[(checkin_station, endStation)][1] += (t-checkin_time)
        else:
            self.total[(checkin_station, endStation)] = [1, (t-checkin_time)]
    def getAverageTime(self, checkin_station: str, endStation: str) -> float:
        # average = total value/ number of values
        total_count, total_time = self.total[(checkin_station, endStation)]
        
        return total_time/total_count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)