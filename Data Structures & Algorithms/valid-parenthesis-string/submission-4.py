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
                    if bonus > 0:
                        bonus -= 1
                    else:
                        return False
                else:
                    item = stack.pop()
                    if item != "(":
                        if bonus > 0:
                            bonus -= 1
                        else:
                            return False
        
        return len(stack) == 0 or len(stack) < bonus