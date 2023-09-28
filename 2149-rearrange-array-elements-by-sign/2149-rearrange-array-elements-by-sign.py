class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        """
        nums = [-5,1,-3,-2,4,6]
        output = [1,-5,4,-3,6,-2]
        output = [1,-5,4,-3,6,-2]
                       |   pos
                     /
        """
        output = [1] * len(nums) #[1,1,1,1,1,1] TC:O(n)
        pos = 0
        neg = 1
        
        for el in nums: #TC: O(n)
            if el > 0:
                output[pos] = el
                pos += 2
            else:
                output[neg] = el
                neg += 2
        return output
            
        
        