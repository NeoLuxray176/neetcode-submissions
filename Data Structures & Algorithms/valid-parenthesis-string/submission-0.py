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
                    return False
                item = stack.pop()
                if item != "(":
                    return False
        
        return len(stack) <= bonus