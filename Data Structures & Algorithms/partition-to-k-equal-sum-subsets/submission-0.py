class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        if sum(nums) % k != 0:
            return False

        n = len(nums)
        target = sum(nums) // k
        nums.sort(reverse=True)

        def backtrack(start : int, parts : List[int]) -> bool:
            if start == n:
                for part in parts:
                    if part != target:
                        return False
                return True

            for i in range(k):
                if parts[i] + nums[start] > target:
                    continue
                if i > 0 and parts[i] == parts[i - 1]:
                    continue
                parts[i] += nums[start]
                if backtrack(start + 1, parts):
                    return True
                parts[i] -= nums[start]
            return False

        return backtrack(0, [0] * k)