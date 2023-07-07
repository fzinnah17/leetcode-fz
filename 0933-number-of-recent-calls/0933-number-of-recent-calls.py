class RecentCounter(object):
    def __init__(self):
        self.output = []

    def ping(self, t):
        self.output.append(t)
        while self.output[0] < t - 3000:
            self.output.pop(0)
        return len(self.output) 
        

"""
    Understand:
We are given an empty array to store the timestamps of incoming ping requests. The goal is to implement a class that has a ping method. This method takes a timestamp as input and returns the number of ping requests made within the last 3000 milliseconds, including the current timestamp. In other words, we need to maintain a sliding time window of 3000 milliseconds and count the number of ping requests falling within that window. Initially, the array is empty. When we make the first ping at timestamp 1, there are no previous pings, so the result is 1. Then, when we make a ping at timestamp 100, the range of valid requests becomes [1, 100] as per the sliding time window of 3000 milliseconds. Therefore, the result is 2 because we have two timestamps within that range. Similarly, for timestamps 3001 and 3002, the range of valid requests becomes [1, 100, 3001] and [2, 3002], respectively. In both cases, the result is 3 as there are three timestamps falling within the sliding time window.

    Match: 
 This problem involves processing and counting elements within a time window. It involves maintaining a window of elements and sliding it over the input to perform calculations efficiently. Using a queue or deque data structure to store and manage the timestamps of the ping requests.
 
    Plan/Pseudocode: ** variable names, function calls, and method invocations providing more specific details about the operations performed **
    1. In the initialization method:
        a. Create an empty list to store the ping requests that will be later returned as an output. Initialize output as an empty list output = [] 
    2. For the ping method, 
        a. Append the timestamp 't' to the output list. 'output.append(t)'
        b. Iterate through the request list left to right: (while loop)
            - IF the timestamp requests[0] < t - 3000:
                remove the left most element from the list to keep only the valid requests within the time window: pop(0)
    3. Return the length of the list
    TC in initialization method: O(1) SC: O(n) for creating a list.
    TC in ping method is O(n) for traversing the array left to right SC: O(n) as we are returning the list"""
# Your RecentCounter object will be instantiated and called as such:
# obj = RecentCounter()
# param_1 = obj.ping(t)