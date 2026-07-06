class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = []  # Stores indices of '('
        bonus = []  # Changed from int to list: Stores indices of '*'

        for i, c in enumerate(s):  # We need the index 'i' now
            if c == "*":
                bonus.append(i)    # Store index instead of just counting
            elif c == "(":
                stack.append(i)    # Store index instead of string "("
            elif c == ")":
                if stack:
                    stack.pop()    # Your logic: Try stack first
                elif bonus:
                    bonus.pop()    # Your logic: Try bonus second
                else:
                    return False   # Nothing left to match ')'

        # Final Check: Match remaining '(' with '*'
        # This replaces your 'len(stack) < bonus' check
        while stack and bonus:
            # If the open paren is AFTER the star, it's invalid.
            # e.g. "*(", stack=[1], bonus=[0]. 1 > 0, so False.
            if stack[-1] > bonus[-1]:
                return False
            stack.pop()
            bonus.pop()

        return len(stack) == 0