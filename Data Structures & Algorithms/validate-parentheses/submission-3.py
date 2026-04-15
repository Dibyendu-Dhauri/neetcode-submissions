class Solution:
    def isValid(self, s: str) -> bool:
        brackets_map ={ ")" : "(", "]" : "[", "}" : "{" }
        stack = []
        for ch in s:
            if ch in brackets_map:
                if stack and stack[-1] == brackets_map[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
                
        
        return True if not stack else False