class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        mp = {0:1}
        cnt = 0
        curr_sum = 0
        for num in nums:
            curr_sum += num
            
            cnt += mp.get(curr_sum - k , 0)

            mp[curr_sum] = mp.get(curr_sum,0) + 1
        return cnt