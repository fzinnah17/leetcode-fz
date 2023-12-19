class Solution:
    def longestConsecutive(self, nums):
        if not nums:
            return 0

        numsSet = set(nums)
        res = 0
        
        for i in range(len(nums)):
            if nums[i] - 1 not in numsSet:
                length = 1
                next_num = nums[i] + 1

                # Using a for loop to check for consecutive numbers
                for j in range(1, len(numsSet)):
                    if next_num in numsSet:
                        length += 1
                        next_num += 1
                    else:
                        break

                res = max(res, length)

        return res
