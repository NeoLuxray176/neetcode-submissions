class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for curr in strs:
            res.append(str(len(curr)) + "#" + curr)

        return "".join(res)

    def decode(self, s: str) -> List[str]:
        # print(s)
        res = []
        i = j = 0
        
        while i < len(s):
            if s[i] == "#":
                length = int(s[j:i])
                # print("Adding", s[i+1:i+1+length])
                res.append(s[i + 1 : i + 1 + length])
                j = i + 1 + length
                i = i + 1 + length
            else:
                i += 1
                

        return res


