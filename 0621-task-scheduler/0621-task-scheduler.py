class Solution(object):
    def leastInterval(self, tasks, delay):
        """
        we are looking for the length
        task: optimize the idle tasks
        algorithm broken down: to idle time will be least possible
        starting with the most frequent elements would reduce the idle time
        """
        freq = [0] * 26
        
        for i in tasks:
            taskIdx = ord(i) - ord('A')
            freq[taskIdx] += 1
        freq.sort()
        maxFreq = freq.pop()
        
        idleTime = (maxFreq - 1) * delay
        
        while freq:
            currFreq = freq.pop()
            idleTime = idleTime - min(currFreq, maxFreq - 1)
            idleTime = max(idleTime, 0)
        return idleTime + len(tasks)
        