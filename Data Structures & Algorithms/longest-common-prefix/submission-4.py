class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = strs[0]

        for s in strs:
            temp = ""
            for i in range(len(s)):
                if i < len(ans) and s[i] == ans[i]:
                    temp += s[i]
                else:
                    break
            ans = temp
        return ans