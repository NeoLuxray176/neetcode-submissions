class Solution:

    def encode(self, strs: List[str]) -> str:
        res = []
        for word in strs:
            for charac in word:
                if charac == "/":
                    res.append("//")
                elif charac == "#":
                    res.append("/#")
                else:
                    res.append(charac)
            res.append("#")
        res = "".join(res)
        # print(res)
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        curr = []

        n = len(s)
        i = 0

        while i < n:
            # print(f"{i} is equal to {s[i]}")
            if s[i] == "#":
                res.append("".join(curr))
                curr = []
                i += 1
            elif s[i] == "/":
                if s[i + 1] == "/":
                    curr.append("/")
                else:
                    curr.append("#")
                i += 2
            else:
                curr.append(s[i])
                i += 1
            
        # print(res)
        return res



