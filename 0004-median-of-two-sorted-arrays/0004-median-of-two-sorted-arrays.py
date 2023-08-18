class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        for i in nums2: #O(n)
            nums1.append(i)
        nums1.sort() #O(nlogn)

        #O(1)
        if (len(nums1) % 2 != 0): #odd
            return float(nums1[len(nums1) // 2])
        else: #even
            prev = float(nums1[(len(nums1) // 2) - 1])
            curr = float(nums1[len(nums1) // 2])
            return float((prev + curr) / 2)