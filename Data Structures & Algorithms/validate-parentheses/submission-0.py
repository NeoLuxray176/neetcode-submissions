class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        open_brackets = {"(", "{", "["}

        for c in s:
            if c in open_brackets:
                stack.append(c)
            else:
                last_open = stack.pop()
                if c == ")" and last_open == "(":
                    continue
                if c == "}" and last_open == "{":
                    continue
                if c == "]" and last_open == "[":
                    continue
                
                return False
        
        return True
        