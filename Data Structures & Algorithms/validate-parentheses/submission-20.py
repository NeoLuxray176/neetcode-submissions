class Solution:
    def isValid(self, s: str) -> bool:
        mp = {"(" : ")", "[" : "]", "{" : "}"}

        stack = []

        for c in s:
            if c in mp.keys():
                stack.append(c)
            else:
                if not stack:
                    return False
                if stack and mp[stack[-1]] != c:
                    return False
                else:
                    stack.pop()

        return not stack