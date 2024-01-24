class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
      multRight = []
      multLeft = []

      # Create the multRight array
      prevVal = nums[0]
      multRight.append(prevVal)

      for n in range(1, len(nums)):
          prevVal *= nums[n]
          multRight.append(prevVal)

      # Create the multLeft array
      prevVal = nums[-1]
      multLeft.append(prevVal)

      for n in range(len(nums) - 2, -1, -1):
          prevVal *= nums[n]
          multLeft.append(prevVal)

      result = []
      for i in range(len(nums)):
          left = 1 if i == 0 else multRight[i - 1]
          right = 1 if i == len(nums) - 1 else multLeft[len(nums) - i - 2]
          result.append(left * right)

      return result

        