class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l = r = 0
        expected_freq , window_freq = [0] * 26, [0] * 26
        for c in s1:
            expected_freq[ord(c) - ord('a')] += 1
        
        while r < len(s2):
            window_freq[ord(s2[r]) - ord('a')] += 1

            if r - l + 1 == len(s1):
                if expected_freq == window_freq:
                    return True
                window_freq[ord(s2[l]) - ord('a')] -= 1
                l += 1
            r += 1
        return False