class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            curr = 1
            for j in range(i, n):
                curr *= nums[j]
                if curr < k:
                    res += 1
                else:
                    break

        return res