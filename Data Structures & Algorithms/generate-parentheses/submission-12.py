class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []


        def dfs(path : List[str], opened : int, closed : int):
            if opened == n and closed == n:
                output = "".join(x for x in path)
                res.append(output)

            if opened < n:
                path.append("(")
                dfs(path, opened + 1, closed)
                path.pop()
            if closed < opened and closed < n:
                path.append(")")
                dfs(path, opened, closed + 1)
                path.pop()

            return

        dfs([], 0, 0)

        return res