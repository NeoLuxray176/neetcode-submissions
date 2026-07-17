class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        
        def dfs(i):

            best = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))

            return best

        res = 0
        for i in range(n):
            res = max(res, dfs(i))

        return res