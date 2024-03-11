class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        # Initialize Hash Table
        hashTable = defaultdict(int)

        # Iterate through numbers: Count each number
        for num in arr:
            hashTable[num] += 1
        
        # Return if duplicate values exist in hash table
        return len(list(hashTable.values())) == len(set(hashTable.values()))