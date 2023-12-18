class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numMap = {}
        
        for i in range(len(nums)):
            if nums[i] not in numMap:
                numMap[nums[i]] = 1
            else:
                numMap[nums[i]] += 1
        
        # Sort the dictionary items by their values (frequencies) in descending order
        sorted_items = sorted(numMap.items(), key=lambda x: x[1], reverse=True)
        
        # Extract the keys (elements) corresponding to the first k items
        result = [item[0] for item in sorted_items[:k]]
        
        return result
