from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = defaultdict(list)
        for ch in strs:
            freq = [0] * 26
            for c in ch:
                freq[ord(c) - ord('a')] += 1
            mp[tuple(freq)].append(ch)
        return list(mp.values())