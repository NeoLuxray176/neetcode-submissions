class Solution:
    ALPHABET_SIZE = 26

    def checkInclusion(self, s1: str, s2: str) -> bool:
        """True iff some substring of s2 is a permutation of s1.

        Assumes both strings consist only of lowercase letters a-z.
        Time O(len(s1) + len(s2)), space O(1).
        """
        n = len(s1)
        if n > len(s2):
            return False

        base = ord('a')

        # need[c]   = how often letter c occurs in s1
        # window[c] = how often it occurs in the current window of s2
        need = [0] * self.ALPHABET_SIZE
        window = [0] * self.ALPHABET_SIZE
        for i in range(n):
            need[ord(s1[i]) - base] += 1
            window[ord(s2[i]) - base] += 1

        # Number of letters whose two counts agree. The window is a
        # permutation of s1 exactly when all 26 agree.
        matches = sum(need[c] == window[c] for c in range(self.ALPHABET_SIZE))

        def shift(char: str, delta: int) -> None:
            """Add delta to the window count of char, keeping matches correct."""
            nonlocal matches
            c = ord(char) - base
            # Only this letter's agreement status can change, so drop its
            # contribution, apply the change, then re-add it.
            if need[c] == window[c]:
                matches -= 1
            window[c] += delta
            if need[c] == window[c]:
                matches += 1

        if matches == self.ALPHABET_SIZE:
            return True

        # Slide a window of fixed width n one position at a time.
        for r in range(n, len(s2)):
            shift(s2[r], 1)       # letter entering on the right
            shift(s2[r - n], -1)  # letter leaving on the left
            if matches == self.ALPHABET_SIZE:
                return True

        return False