class UndergroundSystem:

    def __init__(self):
        self.checkinMap = {}
        self.travelMap = {} #key = route taken, value = totalTime, count

    def checkIn(self, passengerId: int, checkInstation: str, checkIntime: int) -> None:
        self.checkinMap[passengerId] = (checkInstation, checkIntime)   

    def checkOut(self, passengerId: int, checkOutstation: str, checkOuttime: int) -> None:
        startStation, startTime = self.checkinMap[passengerId]
        route = (startStation, checkOutstation)
        totalTime = checkOuttime - startTime
        if route not in self.travelMap:
            self.travelMap[route] = [0,0]
        self.travelMap[route][0] += totalTime
        self.travelMap[route][1] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        route = (startStation, endStation)
        time, count = self.travelMap[route]
        avgTime = time / count
        return avgTime

# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(passengerId,checkInstation,checkIntime)
# obj.checkOut(passengerId,checkOutstation,checkOuttime)
# param_3 = obj.getAverageTime(startStation,endStation)