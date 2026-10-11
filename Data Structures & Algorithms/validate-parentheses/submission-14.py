class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(" : ")", "[" : "]", "{" : "}"}

        for character in s:
            if character in pairs.keys():
                stack.append(character)
            else:
                if not stack:
                    return False
                
                if pairs[stack[-1]] != character:
                    return False
                else:
                    stack.pop()

        return True
