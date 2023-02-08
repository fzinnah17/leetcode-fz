class Solution(object):
    def twoSum(self, numbers, target):        
        """
        pointers = bounds   ----> left, right
        middle
        if middle > target : right -= 1
        if middle < target: left += 1
        THIS IS A 1-INDEXED ARRAY SO GOTTA ADD 1 WITH THE INDICES
        """
        
        for i in range(len(numbers)):
            newTarget = target - numbers[i]
            left = i + 1
            right = len(numbers) - 1
            while left <= right:
                middle = left + ((right - left)//2)

                if numbers[middle] > newTarget:
                    right = middle - 1

                elif numbers[middle] < newTarget:
                    left = middle + 1
                else:
                    return [i+ 1, middle + 1]
                
#         #TC: O(nlogn)  SC: O(1)




"""ANOTHER APPROACH WITH O(N) TIME AND O(1) SPACE:
        left, right = 0, len(numbers) - 1
        while left <= right:
            addition = numbers[left] + numbers[right]
            if addition > target:
                right -= 1
            elif addition < target:
                left += 1
            else:
                return [left + 1, right + 1] #because this is a 1-indexed array
        #TC: O(N) SC: O(1)
        """
        
            
        