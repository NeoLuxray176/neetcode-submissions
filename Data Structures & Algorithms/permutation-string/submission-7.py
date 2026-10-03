class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False
        needed = [0] * 26
        current = [0] * 26
        left = 0

        for character in s1:
            needed[ord(character) - ord("a")] += 1

        for right, character in enumerate(s2):
            current[ord(character) - ord("a")] += 1

            if right >= len(s1):
                current[ord(s2[right - len(s1)]) - ord("a")] -= 1

            if needed == current:
                return True

        return False
