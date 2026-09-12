class Solution:
    def is_pali(self, s : str) -> bool:
        left, right = 0, len(s) - 1
        while left <= right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True

    def partition(self, s: str) -> List[List[str]]:
        res = []

        def backtrack(path : List[str], remain : str):
            if not remain:
                res.append(path)
                return

            for i in range(1, len(remain) + 1):
                if self.is_pali(remain[:i]):
                    backtrack(path + [remain[:i]], remain[i:])
        
        backtrack([], s)
        return res

        