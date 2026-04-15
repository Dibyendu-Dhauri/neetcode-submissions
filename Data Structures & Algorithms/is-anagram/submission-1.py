class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        map_s, map_t = {},{}
        for ch in s:
            map_s[ch] = map_s.get(ch,0) + 1
        for ch in t:
            map_t[ch] = map_t.get(ch,0) +1
        
        return True if map_s == map_t else False