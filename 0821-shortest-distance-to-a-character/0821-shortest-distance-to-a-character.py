class Solution:
  def shortestToChar(self, s, c):
    ans = []
    for i in range(len(s)):
      min_distance = float('inf')  # Set initial distance to positive infinity
      for j in range(len(s)):
        if s[j] == c:
          closest = abs(i - j)
          min_distance = min(min_distance, closest)
      ans.append(min_distance)  # Append the minimum distance for current index
    return ans
