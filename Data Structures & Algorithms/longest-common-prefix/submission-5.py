class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        res = strs[0]

        for string in strs:
            res = res[:len(string)]
            for i in range(min(len(res), len(string))):
                # print(f"Checking {i} {res[i]} {string[i]}")
                if res[i] != string[i]:
                    # print(f"Cut at {i}")
                    res = res[:i]
                    break

        return res