class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        mp = {"(" : ")", "[" : "]", "{" : "}"}

        for character in s:
            if character in ["(", "[", "{"]:
                stack.append(character)
            else:
                if stack and character == mp[stack[-1]]:
                    stack.pop()
                else:
                    return False

        return True
