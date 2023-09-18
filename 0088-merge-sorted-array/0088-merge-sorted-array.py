class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        O(n+m)
        Pseudocode:
        1. copy
        2. pointers(3)
        3. while loop [pointer nums1copy] and [pointer nums2]
            conditional checks:
                [pointer nums1copy] < [pointer nums2]
                    nums1 get the nums1copy
                    nums1copy pointer += 1
                else:
                    nums1 get the nums2
                    nums2 pointer += 1
            pointer to write += 1??
            return nums1
        4. edge cases:
            copy still has elements left
            nums2 still has elements left
            TC: 0(m + n) SC: O(m*n)
        """
        numCopy = nums1[:m]
        readOne, readTwo, writeOne = 0,0,0
        #pointer doesnt exceed
        while readOne < m and readTwo < n:
            if numCopy[readOne] < nums2[readTwo]:
                nums1[writeOne] = numCopy[readOne]
                readOne += 1
            else:
                nums1[writeOne] = nums2[readTwo]
                readTwo += 1
            writeOne += 1
        # If nums1Copy still has values, append them
        while readOne < m:
            nums1[writeOne] = numCopy[readOne]
            readOne += 1
            writeOne += 1
        
        while readTwo < n:
            nums1[writeOne] = nums2[readTwo]
            readTwo += 1
            writeOne += 1
        return nums1
        
        