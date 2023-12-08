class Solution:
    def carFleet(self, target: int, pos: List[int], speed: List[int]) -> int:
        """
        {
        10 : 2
        8 : 4
        0 : 1
        5 : 1
        3 : 3}
    check if k + v is same to any other k + v, then fleet += 1
    even if not fleet += 1 as car itself is a fleet
        """
        cMap = {}
        res = 0
        
        for i in range(len(pos)):
            key = pos[i]
            val = speed[i]
            cMap[key] = val
        # print(cMap) {10: 2, 8: 4, 0: 1, 5: 1, 3: 3}
        sortCars = sorted(cMap.items(), reverse = True)
        # print(sortCars)
        
        maxTime = 0
        
        for p, s in sortCars:
            reachTime = (target - p) / s
            
            if reachTime > maxTime:
                res += 1
                maxTime = reachTime
        return res