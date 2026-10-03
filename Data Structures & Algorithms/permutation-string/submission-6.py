class Solution:
    def cti(self, s1 : str):
        return ord(s1[0]) - ord("A")
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Task
        # Constraints
        # General Idea:
        # In order to track a permutation we can track the number of occurances of each character
        # 

        if len(s1) > len(s2):
            return False

        need = [0] * 26
        window = [0] * 26
        for c in s1:
            need[ord(c) - ord("a")] += 1

        for i, char in enumerate(s2):
            window[ord(char) - ord("a")] += 1
            if i >= len(s1):
                window[ord(s2[i - len(s1)]) - ord("a")] -= 1
            if i + 1 >= len(s1) and need == window:
                return True

        return False



