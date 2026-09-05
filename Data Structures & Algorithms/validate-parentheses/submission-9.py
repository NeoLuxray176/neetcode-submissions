class Solution:
    def isValid(self, s: str) -> bool:
        # Go through the string and for every open bracket we encounter
        # add the corresponding close bracket to the stack.
        # If we encounter a close bracket in the string, check whether it matches what is on
        # top of the stack. If it is we can continue with the next character in the string
        # otherwise the string is not valid.

        stack = []

        for cha in s:
            if cha == "(":
                stack.append(")")
            if cha == "[":
                stack.append("]")
            if cha == "{":
                stack.append("}")
            
            if cha == ")" or cha == "]" or cha == "}":
                if stack and stack[-1] == cha:
                    stack.pop()
                else:
                    return False

        return not stack