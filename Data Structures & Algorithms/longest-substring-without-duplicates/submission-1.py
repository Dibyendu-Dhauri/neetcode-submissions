class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        ans = 0
        window = {}
        while r < len(s):

            if s[r] in window and window[s[r]] >= l:
                l = window[s[r]] + 1

            window[s[r]] = r
            ans = max(ans, r -l + 1)
            r += 1
        return ans