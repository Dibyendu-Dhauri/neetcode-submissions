class Solution:
    def validPalindrome(self, s: str) -> bool:
        l,r = 0, len(s) -1

        while l < r:
            if s[l] != s[r]:
                # take the substring from l+1 to r, and reverse it, to check if it's a plindrome or not
                # take the substring from l to r-1, and reverse it, to check if it's a plindrome or not
                subL = s[l+1:r+1]
                subR = s[l:r]
                return subL == subL[::-1] or subR == subR[::-1]
            l,r = l+1, r-1
        return True
                    