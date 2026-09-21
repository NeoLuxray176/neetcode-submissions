class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # nums=[-1,-1,0,0,-1,-1] # expect 2
        n = len(nums)
        prefix_sum = [0] * n
        # prefix_sum[0] = nums[0]
        suffix_sum = [0] * n
        # prefix_sum[-1] = nums[-1]
        

        for i in range(1, n):
            prefix_sum[i] = prefix_sum[i - 1] + nums[i - 1]
        for i in range(n - 2, -1, -1):
            suffix_sum[i] = suffix_sum[i + 1] + nums[i + 1]
            if prefix_sum[i] == suffix_sum[i]:
                return i

        return -1