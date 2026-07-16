class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        su = sum(nums)

        if su % 2 != 0:
            return False

        def dfs(i, target):
            if i >= n:
                return target == 0
            if target < 0:
                return False

            return dfs(i + 1, target) or dfs(i + 1, target - nums[i])

        return dfs(0, su // 2)