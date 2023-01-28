class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        A set is an unordered collection of objects that doesn’t allow duplicate elements. Typically, sets are used to quickly test a value for membership in the set, to insert or delete new values from a set, and to compute the union or intersection of two sets.

In a proper set implementation, membership tests are expected to run in fast O(1) time. Union, intersection, difference, and subset operations should take O(n) time on average. 
        """
        
        s= set(nums)
        if len(nums) != len(s):
            return True
        return False #TC: O(1) , SC: O(N)
    
        # print(set(nums)) #[1,2,3]
        # print(len(set(nums))) #3
        
        
        #TC & SC: O(N)
#         hashMap = {}
#         for i in nums:
#             if i in hashMap:
#                 hashMap[i] += 1
#                 if hashMap[i] > 1:
#                     return True
#             else:
#                 hashMap[i] = 1
#         return False