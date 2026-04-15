class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        map_t, window = {},{}

        left = right = 0

        for c in t:
            map_t[c] = map_t.get(c,0) + 1
        
        have,need = 0, len(map_t)

        res, resLen = [-1,-1], float("inf")
        while right < len(s):
            window[s[right]] = window.get(s[right],0) + 1

            if s[right] in map_t and window[s[right]] == map_t[s[right]]:
                have += 1
            
            while have == need:
                if (right - left + 1) < resLen:
                    resLen = right - left + 1
                    res = [left,right]
                window[s[left]] -= 1
                if s[left] in map_t and window[s[left]] < map_t[s[left]]:
                    have -= 1
                left += 1
            right += 1
        l,r = res
        return s[l:r+1] if resLen != float("inf") else ""