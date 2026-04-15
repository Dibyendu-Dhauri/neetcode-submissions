from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        heap = []
        for key,val in freq.items():
            heapq.heappush(heap,(-val,key))
        
        ans = []
        while k:
            val,key = heapq.heappop(heap)
            ans.append(key)
            k -= 1
        return ans