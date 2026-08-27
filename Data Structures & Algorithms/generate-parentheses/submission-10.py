class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        res = []

        def dfs(path : [str], opened : int, closed :int):
            print(f"dfs first {opened} {closed}")
            if opened == n and closed == n:
                print("Finish")
                output = "".join(x for x in path)
                res.append(output)

            if opened < n:
                print("Open bracket")
                path.append("(")
                dfs(path, opened + 1, closed)
                path.pop()
            if opened < closed and closed < n:
                print("Close bracket")
                path.append(")")
                dfs(path, opened, closed + 1)
            
            print("return")
            return

        dfs([], 0, 0)

        return res