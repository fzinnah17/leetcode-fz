class Solution(object):
    def twoSum(self, nums, target):
        """
        Pseudocode:
        1. Create a hash table/dict
        value : index
        2. iterate over the nums array to have both index and the value and fill in the hash table
                a. if the values are found, return:
                        [dictionary[found value], current index]
                b. if not found, then assign:
                        dictionary[value] = index
        TC: O(n) for loop SC: O(n) dictionary
        """
        numDict = {} #key = nums[i] = v value = i(index)
        # value : index
        for index, value in enumerate(nums):
            complement = target - value #complement is another value that I am looking for so treat it as a regular value
            if complement in numDict:
                return [numDict[complement], index]
            numDict[value] = index
            
        
        