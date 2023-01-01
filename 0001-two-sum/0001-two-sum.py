class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        
        1. dictionary : {2:0}
        2. for loop
        sub = target - num[i]
        9 - 2 = 7
        if not dict:
        dict[num[i]]
        
        if in dict:
        
        

        """
        ''' nums = [2,7,11,15], target = 9
        nums = [3,2,4], target = 6
        map {
        3 : 0
        2 : 1
       
         
        }
        
        '''
              

        hashMap = {}
        for i in range(len(nums)):
            sub = target - nums[i]
            if sub in hashMap:
                return [hashMap[sub],i]
            hashMap[nums[i]] = i
            
        return []

                
        
        