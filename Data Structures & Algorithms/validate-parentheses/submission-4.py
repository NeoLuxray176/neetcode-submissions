class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for paren in s:
            if paren in ['(', "{", "["]:
                stack.append(paren)
            else:
                if not stack:
                    return False
                last = stack.pop()
                if last == '(':
                    if paren != ')':
                        return False
                if last == "{":
                    if paren != "}":
                        return False
                if last == "[":
                    if paren != "]":
                        return False
        
        return True