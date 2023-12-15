class Solution:
    def smallestRangeI(self, nums: List[int], k: int) -> int:
        """       
            Example 1 -> nums = [0,10], k = 2
            choosing i means
            i -> [0, len(nums) = 2]
            let's choose 10
            change 10 to 10 + x [x:{-2, -1, 0, 1, 2}]
            it can be done once only for 10
            10 - 2 = 8
            10 - 1 = 9
            10 - 0 = 10
            10 + 1 = 11
            10 + 2 = 12
            
            for 0,
                0 - 2 = -2
                0 - 1 = -1
                0 + 0 = 0
                0 + 1 = 1
                0 + 2 = 2
            
            for -2, 8 + 2 = 10
            for - 1, 9 + 1 = 10
            for 0, 10 - 0 = 10
            for 1, 11 - 1 = 10
            for 2, 12 - 2 = 10
                        
            return: minimum score of nums after taking i and adding x to it
            
            minimum from the operations of 10 is 8
            maximum from the operations of 0 is 2,
            
            so 8 - 2 = 6 return
            
            Pseudocode:
            1. iterater over nums
                a. for each i,
                    take the value + [-k, k] store it inside a list
                do it until we reach the end of the given srray
            2. take the minimum of the highest array value list
            3. take the maximum of the lowest array value of the list
            4. subtract those and return it
            
            """
        lowerList = []
        upperList = []
        for i in range(len(nums)):
            lowerBound = nums[i] - k
            lowerList.append(lowerBound)
            upperBound = nums[i] + k
            upperList.append(upperBound)
        maxLower = max(lowerList)
        minUpper = min(upperList)
        
        score = maxLower - minUpper
        return max(0, score)
            