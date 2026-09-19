class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need, window = [0] * 26, [0] * 26
        for char in s1:
            need[ord(char) - ord("a")] += 1
        for i, char in enumerate(s2):
            window[ord(char) - ord("a")] += 1
            if i >= len(s1):
                window[ord(s2[i - len(s1)]) - ord("a")] -= 1
            # Window is valid and the window and need agree
            if i + 1 >= len(s1) and need == window:
                return True

        return not s1