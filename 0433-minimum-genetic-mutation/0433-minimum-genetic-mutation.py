class Solution(object):
    def minMutation(self, start, end, bank):
        def helper(stringOne, stringTwo):
            differences = 0
            curr_index = 0
            while curr_index < min(len(stringOne), len(stringTwo)):
                if stringOne[curr_index] != stringTwo[curr_index]:
                    differences += 1
                curr_index += 1
            return differences
        
        myQueue = deque() #prints out deque([])
        myQueue.append((start,0)) #deque([('AACCGGTT', 0)])
        seen = set() #set([])
        seen.add(start) #set(['AACCGGTT'])
        
        while myQueue:
            checkString, nextString = myQueue.popleft() #('AACCGGTT', 0)
            if checkString == end:
                return nextString
            for existString in bank:
                if helper(checkString, existString) == 1 and existString not in seen:
                    seen.add(existString)
                    myQueue.append((existString, nextString + 1))
        return -1
        
            
        