class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []

        i, j = 0, 0

        while i < len(word1) and j < len(word2):
            if i <= j:
                res.append(word1[i])
                i += 1
            else:
                res.append(word2[j])
                j += 1

        if i < len(word1):
            res.append(word1[i:])
        if j < len(word2):
            res.append(word2[j:])

        return "".join(res)