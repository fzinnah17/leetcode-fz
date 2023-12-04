class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nMap = defaultdict(int)
        for e in nums:
            if e not in nMap:
                nMap[e] = 1
            else:
                nMap[e] += 1
        # print(nMap)
        topK = sorted(nMap, key = nMap.get, reverse = True)[:k]
        # return 
        # print(nMap)
        # print()
        # print(topK)
        return topK

        # res = list(nMap.keys())[:k]
        # return res
        