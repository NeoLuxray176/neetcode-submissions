class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n = len(s1)
        if n > len(s2):
            return False

        base = ord('a')

        need = [0] * 26
        window = [0] * 26

        for i in range(n):
            need[ord(s1[i]) - base] += 1
            window[ord(s2[i]) - base] += 1

        matches = sum(need[c] == window[c] for c in range(26))

        left = 0
        for right in range(len(s1), len(s2)):
            if matches == 26:
                return True

            window[ord(s2[right]) - base] += 1
            if need[ord(s2[right]) - base] == window[ord(s2[right]) - base]:
                matches += 1
            elif need[ord(s2[right]) - base] + 1 == window[ord(s2[right]) - base]:
                matches -= 1

            window[ord(s2[left]) - base] -= 1
            if need[ord(s2[left]) - base] == window[ord(s2[left]) - base]:
                matches += 1
            elif need[ord(s2[left]) - base] - 1 == window[ord(s2[left]) - base]:
                matches -= 1

            left += 1

        return matches == 26
