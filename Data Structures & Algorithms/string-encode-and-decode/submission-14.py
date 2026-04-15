class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for s in strs:
            len_s = len(s)
            encoded_str += str(len_s)
            encoded_str += '#'
            encoded_str += s
        return encoded_str

    def decode(self, s: str) -> List[str]:
        ans = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1

            len_str = int(s[i:j])
            i = j + 1
            j = i + len_str

            ans.append(s[i:j])
            i = j
        
        return ans