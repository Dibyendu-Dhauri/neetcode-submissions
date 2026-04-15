class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res +=  str(len(s)) + '#'  + s
        return res
    def decode(self, res: str) -> List[str]:
        ans = []
        i = 0
        while i < len(res):
            j = i
            while res[j] != '#':
                j+= 1
            length = int(res[i:j])
            i = j + 1
            j = i + length
            ans.append(res[i:j])
            i = j
        return ans