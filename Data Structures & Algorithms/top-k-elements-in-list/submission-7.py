class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []
        for num in freq:
            heapq.heappush(heap,(freq[num],num))
            if len(heap) > k:
                heapq.heappop(heap)
        
        res = []
        while heap:
            res.append(heapq.heappop(heap)[1])
        return res