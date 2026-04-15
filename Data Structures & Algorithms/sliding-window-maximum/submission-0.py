class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        ans = []
        left = right = 0
        window = {}
        maxi = float("-inf")
        while right < len(nums):
            window[nums[right]] = window.get(nums[right],0) + 1
            if nums[right] > maxi:
                maxi = nums[right]
            
            if right - left + 1 > k:
                window[nums[left]] -= 1
                if window[nums[left]] == 0:
                    del window[nums[left]]
                
                if nums[left] == maxi:
                    maxi = max(window)
                left += 1

            if right - left + 1 == k:
                ans.append(maxi)
            right += 1
        
        return ans