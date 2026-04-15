class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        ans = 0
        window = set()
        while r < len(s):

            while s[r] in window:
                window.remove(s[l])
                l += 1

            window.add(s[r])
            ans = max(ans, r -l + 1)
            r += 1
        return ans