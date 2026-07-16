class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        def dfs(i, j):
            if i == n:
                return 0

            res = dfs(i + 1, j)
            
            if j == -1 or nums[j] < nums[i]:
                res = max(res, dfs(i + 1, i) + 1)

            return res

        return dfs(0, -1)