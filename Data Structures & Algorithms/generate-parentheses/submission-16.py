class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def backtrack(path : List[str], opened : int, closed : int):
            if opened > n:
                return
            if closed > n:
                return
            if opened == n and closed == n:
                res.append("".join(path[::]))

            if opened < n:
                path.append("(")
                backtrack(path, opened + 1, closed)
                path.pop()
            if closed < opened and opened <= n:
                path.append(")")
                backtrack(path, opened, closed + 1)
                path.pop()
            return

        backtrack([], 0, 0)

        return res