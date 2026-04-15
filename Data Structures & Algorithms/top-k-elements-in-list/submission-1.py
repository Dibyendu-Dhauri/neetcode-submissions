class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = {}
        for num in nums:
            mp[num] = mp.get(num,0) + 1

        heap = []
        for key,values in mp.items():
            heapq.heappush(heap,(values,key))
            if len(heap) > k:
                heapq.heappop(heap)

        ans = []
        for key,value in heap:
            ans.append(value)
        return ans