class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        hashMap = {}
        for i in range(len(nums)):
            if nums[i] not in hashMap:
                hashMap[nums[i]] = i
            else:
                if abs(i - hashMap[nums[i]]) <= k:
                    return True
                else:
                    hashMap[nums[i]] = i
        return False
    """
    Pseducode:
    1. use a hashMap to check if the number already exists
    2. traverse the array
        a. if not in the hashmap, then add it
        b. if in the hashmap:
            i. check if the current index position - previous index position <= k:
                        return True
            ii. if NOT > k:
                        update the previous index position with the current index position
    3. return False if after traversing we see that there are no indices that meet the conditions given
    TC: O(n) SC: O(n)"""