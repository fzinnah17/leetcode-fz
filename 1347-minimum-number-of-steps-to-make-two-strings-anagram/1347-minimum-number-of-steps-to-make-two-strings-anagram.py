from collections import defaultdict
class Solution(object):
    def minSteps(self, s, t):
        hashMap = collections.defaultdict(dict)
        
        for index, value in enumerate(s):
            if not hashMap[value]:
                hashMap[value] = 1
                continue
            hashMap[value] += 1
        
        print(hashMap)
        
        differentChars = 0
        
        for each_index, each_value in enumerate(t):
            if hashMap[each_value]:
                differentChars += 1
                hashMap[each_value] -= 1
        
        return len(t) - differentChars
                
            
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        # hashMap = collections.defaultdict(dict) #{}
        # for i, a in enumerate(s):
        #     if not hashMap[a]:
        #         hashMap[a] = 1
        #         continue
        #     hashMap[a]+=1
        # print(hashMap)
        # replacedChars = 0
        # for i, a in enumerate(t):
        #     if hashMap[a]:
        #         replacedChars += 1
        #         hashMap[a]-=1
        # print(len(t))
        # print(replacedChars)
        # print(len(t) - replacedChars)
        # return len(t) - replacedChars
        #make each string a list
        #then have two pointers iterate thru
        #then if value of t pointer is not matching with the value of the s pointer, then replace the value of t with s character
        #we will have a count and it will go up every time the changes happen
        #at the end return the count
        #but to find anagram check if the count of the characters are the same or not
        
#         s= list(s)
#         t = list(t)
        
#         # print(s,t) -> (['b', 'a', 'b'], ['a', 'b', 'a'])
#         for tcharVal, scharVal in enumerate(zip(t,s)):
#             if tcharVal != scharVal:

        
                
        
        