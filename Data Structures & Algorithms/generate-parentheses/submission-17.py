class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(opened : int, closed : int, path : List[str]):
            if opened == n and closed == n:
                p = "".join(path)
                res.append(p)
                return

            if opened < n:
                path.append("(")
                backtrack(opened + 1, closed, path)
                path.pop()
            if closed < opened and closed < n:
                path.append(")")
                backtrack(opened, closed + 1, path)
                path.pop()

        backtrack(0, 0, [])

        return res