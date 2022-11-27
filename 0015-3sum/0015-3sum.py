class Solution(object):
    def threeSum(self, nums):        
        result = []
        nums.sort() #[-4,-1,-1,0,1]
        result_set = set()
        for curr_index, curr_value in enumerate(nums):
            if curr_index > 0 and curr_value == nums[curr_index - 1]:
                continue #if the current value is same as previous we disregard the nums
                #applicable for -1 and -1
            left, right = curr_index + 1, len(nums)-1
            while left < right:
                total = curr_value + nums[left] + nums[right]
                if total > 0:
                    right -= 1 #larger sum means move down 
                elif total < 0:
                    left += 1 #smaller sum means move up
                else:
                    if (curr_value,nums[left],nums[right]) not in result_set:
                        result.append([curr_value, nums[left], nums[right]])
                        result_set.add((curr_value,nums[left],nums[right]))
                    left += 1 #left pointer
                    right -= 1
        return result
    
                    

                
                
            
        
        