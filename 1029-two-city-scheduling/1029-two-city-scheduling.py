class Solution(object):
    def twoCitySchedCost(self, costs):
        #iterate through the array
        #from each list inside the array, compare both values and then get the
        #minimum value of each list and add it to the sum
        #sum = min(list1val)+min(list2val)+...
        #MY APPROACH WILL BE INVALID BC there has to be n people on each city. So 4 people in city A, 4 people in city B. if all the people goes to city A then it is invalid.
        #costs = [[259,770],[448,54],[926,667],[184,139]]
        costs = sorted(costs, key = lambda x: x[0]-x[1], reverse = True)
        #this prints [[448, 54], [926, 667], [184, 139], [259, 770]]
        #                394        259           45        -511
        #this prints [[259,770],[448,54],[926,667],[184,139]]
        #               -511       394     259        45
        n = len(costs) // 2 #this is to have people on both cities
        sumSofar = 0
        for index in range (2*n):
            if index < n:
                sumSofar += costs[index][1]
            else:
                sumSofar += costs[index][0]
        return sumSofar
        # print(costs)
        

        
        
        