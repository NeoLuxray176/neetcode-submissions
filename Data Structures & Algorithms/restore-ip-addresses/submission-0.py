class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # General Idea
        # Recursive, check if we can add a dot between left and right side
        # We can insert a dot if the left side is not empty and the right side does not start with a zero
        # and the left side is smaller than

        res = []
        if len(s) > 12:
            return res

        def backtrack(i, dots, curIP):
            if dots == 4 and i == len(s):
                res.append(curIP[:-1])
                return
            if dots > 4:
                return

            for j in range(i, min(i + 3, len(s))):
                if i != j and s[i] == "0":
                    continue
                if int(s[i : j + 1]) < 256:
                    backtrack(j + 1, dots + 1, curIP + s[i : j + 1] + ".")
            
        backtrack(0, 0, "")
        return res
            
            