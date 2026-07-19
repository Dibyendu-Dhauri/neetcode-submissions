class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        ans = 0
        window = {}
        max_freq = 0
        while right < len(s):
            window[s[right]] = window.get(s[right],0) + 1
            max_freq = max(max_freq, window[s[right]])

            if (right - left + 1) - max_freq > k:
                window[s[left]] -= 1
                left += 1
            
            ans = max(ans, right - left + 1)
            right += 1
        return ans