class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        count = [0] * 26

        for ch in s:
            count[ord('a') - ord(ch)] += 1
        
        for ch in t:
            count[ord('a') - ord(ch)] -= 1
        
        for num in count:
            if num != 0:
                return False
        return True