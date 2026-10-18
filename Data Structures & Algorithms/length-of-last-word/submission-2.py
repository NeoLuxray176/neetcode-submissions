class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        n = len(s)
        last_word_len = 0

        for i in range(n - 1, -1, -1):
            if s[i] == " " and last_word_len == 0:
                continue
            elif s[i] == " ":
                return last_word_len
            else:
                last_word_len += 1

        return last_word_len
