class Solution:
    def isValid(self, s: str) -> bool:
        mp = {"(" : ")", "{" : "}", "[" : "]"}
        stack = []

        for c in s:
            if c in mp.keys():
                stack.append(c)
            elif c in mp.values():
                if stack and mp[stack[-1]] == c:
                    stack.pop()
                else:
                    return False
            else:
                return False

        return True

