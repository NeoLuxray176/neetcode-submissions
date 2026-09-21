class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""

        res = len(strs[0])

        for string in strs:
            res = min(res, len(string))
            for i, character in enumerate(string):
                if i < res and strs[0][i] != character:
                    res = max(0, i)
                    break

        return strs[0][:res]