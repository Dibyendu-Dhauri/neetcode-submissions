class Solution:
    def isValid(self, s: str) -> bool:
        mp = {'(':')','{':'}','[':']'}
        stack = []

        for c in s:
            if c == '(' or c == '{' or c == '[':
                stack.append(c)
            else:
                if not stack or c != mp[stack[-1]]:
                    return False
                stack.pop()
        return True if not stack else False