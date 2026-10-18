class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        count_s = Counter(s)
        count_t = Counter(t)

        for character in s:
            if character not in count_t:
                return False
            if count_t[character] <= 0:
                return False
            count_t[character] -= 1

        return True