class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(path : List[str], index : int):
            if index >= len(s):
                res.append(path[::])
                return

            for i in range(index, len(s)):
                substr = s[index : i + 1]
                if substr == substr[::-1]:
                    path.append(substr)
                    backtrack(path, i + 1)
                    path.pop()

        backtrack([], 0)

        return res