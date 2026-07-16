class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        cache = [-1] * n

        def dfs(i):
            # length of the LIS starting at (and including) nums[i]
            if cache[i] != -1:
                return cache[i]

            best = 1
            for j in range(i + 1, n):
                if nums[j] > nums[i]:
                    best = max(best, 1 + dfs(j))

            cache[i] = best
            return best

        return max((dfs(i) for i in range(n)), default=0)