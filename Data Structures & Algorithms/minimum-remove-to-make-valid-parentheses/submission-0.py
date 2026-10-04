class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        
        extra = 0
        res = []

        for c in s:
            if c == "(":
                extra += 1
                res.append(c)
            elif c == ")" and extra > 0:
                extra -= 1
                res.append(c)
            elif c != ")":
                res.append(c)

        filtered = []
        for c in reversed(res):
            if c == "(" and extra > 0:
                extra -= 1
            else:
                filtered.append(c)

        return "".join(reversed(filtered))