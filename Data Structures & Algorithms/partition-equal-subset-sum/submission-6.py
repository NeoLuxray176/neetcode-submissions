class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        su = sum(nums)

        if su % 2 != 0:
            return False

        target = su // 2

        cache = [[-1] * (target + 1) for _ in range(n + 1)]

        def dfs(i, target):
            if i >= n:
                return target == 0
            if target < 0:
                return False

            if cache[i][target] != -1:
                return cache[i][target]

            res = cache[i][target] = dfs(i + 1, target) or dfs(i + 1, target - nums[i])

            return res

        return dfs(0, su // 2)