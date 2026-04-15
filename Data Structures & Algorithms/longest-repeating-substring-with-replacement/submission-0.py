class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        l = r = 0
        highest_freq = 0
        window = {}
        ans = 0

        while r < len(s):
            window[s[r]] = window.get(s[r],0) + 1
            highest_freq = max(highest_freq,window[s[r]])
            required_rep = (r - l + 1) - highest_freq

            if required_rep > k:
                window[s[l]] -= 1
                l += 1
            ans = max(ans, r - l + 1)
            r += 1
        return ans
            
