class Solution:
    def checkValidString(self, s: str) -> bool:
        pairs = {
            ")" : "("
        }
        stack = []
        bonus = 0

        for c in s:
            if c == "*":
                bonus += 1
            if c == "(":
                stack.append("(")
            if c == ")":
                if len(stack) < 1:
                    bonus -= 1
                else:
                    item = stack.pop()
                    if item != "(":
                        bonus -= 1
        
        return len(stack) < bonus