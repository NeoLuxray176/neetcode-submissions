class Solution:
    def checkValidString(self, s: str) -> bool:
        low, high = 0, 0

        for character in s:
            if character == "(":
                low += 1
                high += 1
            if character == ")":
                low = max(0, low - 1)
                high -= 1
                if high < 0:
                    return False
            if character == "*":
                low = max(0, low - 1)
                high += 1

        return low == 0