class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = [0] * 26
        for ch in s:
            temp[ord('a') - ord(ch)] += 1
        
        for ch in t:
            temp[ord('a') - ord(ch)] -= 1
        
        for num in temp:
            if num != 0:
                return False
        return True