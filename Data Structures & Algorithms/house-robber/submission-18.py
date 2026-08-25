class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 0:
            return 0

        if n == 1:
            return nums[0]
        if n == 2:
            return max(nums[0], nums[1])

        arr = [0] * (n + 1)
        arr[0], arr[1] = nums[0], max(nums[0], nums[1])

        for i in range(2, n):
            arr[i] = max(arr[i - 2] + nums[i], arr[i - 1])

        return arr[n-1]