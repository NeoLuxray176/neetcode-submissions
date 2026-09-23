class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        n = len(nums)
        for i in range(n):
            for j in range(i + 2, n):
                if sum(nums[i : j + 1]) % k == 0:
                    return True

        return False