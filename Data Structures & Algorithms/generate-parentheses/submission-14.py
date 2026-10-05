class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(curr : List[str], opened : int, closed : int):
            if opened == n and closed == n:
                res.append("".join(curr))
                return

            if opened < n:
                backtrack(curr + ["("], opened + 1, closed)
            if closed < opened and opened <= n:
                backtrack(curr + [")"], opened, closed + 1)

        backtrack([], 0, 0)

        return res