from collections import Counter


class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """Return the shortest substring of s containing every character of t
        (respecting multiplicity), or "" if no such substring exists.

        Time:  O(|s| + |t|) - each index is visited at most twice (once by
               right, once by left).
        Space: O(|s| + |t|) for the two counters.
        """
        if not s or not t:
            return ""

        need = Counter(t)  # required multiplicity per character
        window = Counter()  # current multiplicity inside s[left:right + 1]

        # satisfied = number of distinct characters whose quota the window
        # currently meets. The window is valid exactly when it equals required.
        satisfied = 0
        required = len(need)

        best_start, best_len = 0, float("inf")
        left = 0

        for right, char in enumerate(s):
            window[char] += 1

            # "==" rather than ">=": this fires only on the occurrence that
            # completes the quota, so each character is counted once.
            if char in need and window[char] == need[char]:
                satisfied += 1

            # Shrink from the left as long as the window stays valid. This is
            # what makes the recorded window minimal for this right endpoint.
            while satisfied == required:
                if right - left + 1 < best_len:
                    best_start = left
                    best_len = right - left + 1

                left_char = s[left]
                window[left_char] -= 1
                if left_char in need and window[left_char] < need[left_char]:
                    satisfied -= 1
                left += 1

        if best_len == float("inf"):
            return ""

        return s[best_start : best_start + best_len]