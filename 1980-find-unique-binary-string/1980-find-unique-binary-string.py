class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        res = ""
        
        i = 0
        
        for bin in nums:
            res += str(1 - int(bin[i]))
            i += 1
        return res