class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map, s2_map = [0] * 26, [0] * 26

        left = right = 0
        for ch in s1:
            s1_map[ord(ch) - ord('a')] += 1

        while right < len(s2):
            s2_map[ord(s2[right]) - ord('a')] += 1
            if right - left + 1 == len(s1):
                if s1_map == s2_map:
                    return True
                else:
                    s2_map[ord(s2[left]) - ord('a')] -= 1
                    left += 1

            
            right += 1
        return False