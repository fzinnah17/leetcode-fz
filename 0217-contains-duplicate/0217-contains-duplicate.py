class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
      count = collections. defaultdict (int)
      for n in nums:
        count[n] += 1
        if count [n] > 1: return True
      return False
        