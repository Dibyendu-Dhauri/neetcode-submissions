from collections import Counter
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        map_s = {}
        map_t = {}
        for ch in s:
            map_s[ch] = map_s.get(ch,0) + 1
        for ch in t:
            map_t[ch] = map_t.get(ch,0) + 1
        return map_s == map_t
