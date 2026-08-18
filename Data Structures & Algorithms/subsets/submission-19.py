class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        def dfs(curr: List[int], rest: List[int]):
            if not rest:
                res.append(curr)
                return

            dfs(curr + [rest[0]], rest[1:])
            dfs(curr, rest[1:])

        dfs([], nums)
        return res