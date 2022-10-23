class Solution(object):
    def triangleNumber(self, nums):
        #two pointer:
        #right pointer decrease and as soon as the list has 3 values we can think it is a triangle
        #[2,2,3,4]
        #l    t r
        #triangle list = [2,4,3], [2, 4, 2], [2,3,2] -> how many: 3 traingles count
        
        #[4, 2, 3, 4]
        # l  t  r
        #triangle list [[4,2,4], [4,3,4], [4,2,3], ]
        #as soon as t = r, then r -= 1
        
        # nums.sort() # nums = [4,2,3,4]
        # # print(nums) [2, 3, 4, 4]
        ans = 0
        nums.sort()
        for i in reversed(range(1, len(nums))):
            l, r = 0, i - 1
            while l < r:
                if nums[l] + nums[r] > nums[i]:
                    ans += r - l
                    r -= 1
                else:
                    l += 1
        return ans
        