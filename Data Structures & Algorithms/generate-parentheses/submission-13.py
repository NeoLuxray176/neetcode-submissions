class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path : [str], openP : int, closeP : int):
            if openP == closeP == n:
                res.append("".join(path))
                return

            if openP < n:
                backtrack(path + ["("], openP + 1, closeP)
            if closeP < openP and closeP < n:
                backtrack(path + [")"], openP, closeP + 1)

        backtrack([], 0, 0)
        return res