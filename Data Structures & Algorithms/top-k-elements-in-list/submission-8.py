class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)

        bucket = [[] for _ in range(len(nums)+1)]

        for key,val in freq.items():
            bucket[val].append(key)
        
        ans = []

        for i in range(len(bucket)-1,0,-1):
            for num in bucket[i]:
                ans.append(num)
                if len(ans) == k:
                    return ans