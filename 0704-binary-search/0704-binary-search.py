class Solution:
    def search(self, nums: List[int], t: int) -> int:
        """
        sorted in ascending order
        """
        l, r = 0, len(nums) - 1
        
        while l <= r:
            m = l + ((r - l) // 2)
            
            if nums[m] == t:
                return m
            elif nums[m] > t:
                r = m - 1
            else:
                l = m + 1
        return -1