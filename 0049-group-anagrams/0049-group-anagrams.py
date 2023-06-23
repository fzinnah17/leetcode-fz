class Solution(object):
    def groupAnagrams(self, strs):
        """
        Pseudocode:
        1. variables: result = [] needs to be resetted to empty after the anagrams are grouped but how? ,                      output = [], pointer
        2. edge case: if not array: return empty array
                      if len(array) == 1: return the array
        3. Traverse through each string of the array
            if Counter(i value) != Counter(pointer value):
                pointer += 1
            else:
                add it to the result with result.append()
                pointer += 1
            pointer += 1 (as it will be moving any way)
            the loop will keep on going till the pointer reaches the end of the string    
        TC: O(n) SC: O(n)
        """
        output = []
        result = {}

        if not strs:
            return []
        if len(strs) == 1:
            return [strs]
        for i in range(len(strs)):
            count = Counter(strs[i])
            countTuple = tuple(sorted(count.items()))
            if countTuple not in result:
                result[countTuple] = [strs[i]]
            else:
                result[countTuple].append(strs[i])
        for group in result.values():
            output.append(group)
        return output