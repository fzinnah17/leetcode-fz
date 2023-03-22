class Solution(object):
    def findDifference(self, nums1, nums2):
        """TC: O(1) SC: O(n)"""
        nums1 = set(nums1)
        nums2 = set(nums2)
        #set([-94, -19, -80, 82, 21, -68, -43]), set([-63])
        nums1_unique = nums1 - nums2
        nums2_unique = nums2 - nums1
        #(set([1, 3]), set([4, 6]))
        return [list(nums1_unique), list(nums2_unique)]
    
    
    
    
    
    
    
    
    
        """
        Pseudo-code DIDN'T WORK:
        1. traverse both arrays at the same time using enumerate
        2. check:
            a. if nums1[el] == nums2[el]:
                delete that nums1[el] and nums2[el]
                but my concern is we can't remove from the lists as lists are immutable
        3. Then append the lists inside the output list
        4. return the output
        TC: O(n) SC: O(n)
        
        nums1_unique = []
        nums2_unique = []
        for i, (el1, el2) in enumerate(zip(nums1,nums2)):
            if el1 not in nums2:
                nums1_unique.append(el1)
            if el2 not in nums1:
                nums2_unique.append(el2)           
        return [list(set(nums1_unique)), list(set(nums2_unique))]
"""
        