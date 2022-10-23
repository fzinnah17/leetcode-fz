class Solution(object):
    def triangleNumber(self, nums):
        #[4,2,3,4]
        nums.sort() #[2, 3, 4, 4] -> [4, 4, 3, 2]
        # nums.reverse() #[4, 4, 3, 2]
        result = 0
        for index in reversed(range(1, len(nums))):
            # print(nums[index]) 4 -> 3 -> 2
            left, right = 0, index - 1
            # print(left,right) #-> (0,0) -> (0,1) -> (0,2) (0, index - 1)
            # print(nums[left],nums[right]) #(4,4) -> (4,4) -> (4,3)
            while left < right:
                if nums[left] + nums[right] > nums[index]:
                    result += right - left
                    right -= 1
                else:
                    left += 1
        return result
                    
                    
        