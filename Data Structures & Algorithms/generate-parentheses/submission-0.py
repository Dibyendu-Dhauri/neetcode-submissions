class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        # only add open parenthesis if open < n
        # only add close parenthesis if close < open
        # valid if open == close == n
        subsets = []
        res = []

        def backtrack(openN, closeN):
            if openN == closeN == n:
                res.append("".join(subsets))
                return
            
            if openN < n:
                subsets.append("(")
                backtrack(openN+1,closeN)
                subsets.pop()
            
            if closeN < openN:
                subsets.append(")")
                backtrack(openN, closeN + 1)
                subsets.pop()
        
        backtrack(0,0)
        return res