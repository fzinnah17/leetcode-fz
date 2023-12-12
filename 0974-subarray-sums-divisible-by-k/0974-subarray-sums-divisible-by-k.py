class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        output, preSum = 0, 0
        preFix = { 0 : 1 }
        
        for n in nums:
            preSum += n
            
            rem = preSum % k
            
            output += preFix.get(rem, 0)
            
            preFix[rem] = 1 + preFix.get(rem, 0)
        
        return output
        