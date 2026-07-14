class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []

        stack = []

        def dfs(i):
            if i >= len(nums):
                res.append(stack.copy())
                return

            stack.append(nums[i])
            dfs(i + 1)

            stack.pop()
            dfs(i + 1)

        dfs(0)
        return res