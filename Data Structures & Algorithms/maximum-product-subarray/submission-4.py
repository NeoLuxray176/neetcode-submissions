class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Brute Force: check every sub array

        n = len(nums)

        res = min(nums)

        for i in range(n):
            tmp =  nums[i]
            res = max(tmp, res)
            for j in range(i+1,n):
                tmp *= nums[j]
                res = max(tmp, res)

        return res