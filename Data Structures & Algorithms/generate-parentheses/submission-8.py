class Solution:
    def generateParenthesis(self, n):
        # n pairs means 2n total parenthesis `(` or `)`
        # Valid if we have more at least as many open as closed brackets

        # A decision tree, open or close a bracket
        # recursive backtracking style solution

        # we need to know number of open and closed brackets

        res = []

        def dfs(open : int, closed : int, val : list[str]):
            if open == n and closed == n:
                output = "".join(x for x in val)
                res.append(output)

            if open < n:
                next_val = val.copy()
                next_val.append("(")
                dfs(open + 1, closed, next_val)
            if closed < open and closed < n:
                next_val = val.copy()
                next_val.append(")")
                dfs(open, closed + 1, next_val)
            return

        dfs(0, 0, [])

        return res