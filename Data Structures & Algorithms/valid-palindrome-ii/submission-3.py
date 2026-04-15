class Solution:
    def validPalindrome(self, s: str) -> bool:
        left,right = 0, len(s) -1

        def check_palindrome(l,r):
            while l < r:
                if s[l] != s[r]:
                    return False
                l,r = l+1, r-1
            return True

        while left < right:
            if s[left] != s[right]:
                if not check_palindrome(left+1,right) and not check_palindrome(left,right-1):
                    return False
            
            left,right = left+1, right-1

        return True