class Solution(object):
    def intersection(self, nums1, nums2):
        """
        TC: O(1) SC: O(n)
        """
        nums1 = set(nums1)
        nums2 = set(nums2)
        return nums1 & nums2
            
