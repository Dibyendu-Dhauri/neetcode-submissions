class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        left = right = 0

        ans = ""
        while left < len(word1) and right < len(word2):
            ans += word1[left]
            ans += word2[right]
            left,right = left+1, right + 1
        
        if left < len(word1):
            ans += word1[left:]
        
        if right < len(word2):
            ans += word2[right:]
        
        return ans