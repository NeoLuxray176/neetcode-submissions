class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        if k <= 1:
            return 0

        n = len(nums)
        res = 0
        left, curr = 0, 1

        for right in range(n):
            curr *= nums[right]
            while left <= right and curr >= k:
                curr //= nums[left]
                left += 1
            res += (right - left + 1)

        return res