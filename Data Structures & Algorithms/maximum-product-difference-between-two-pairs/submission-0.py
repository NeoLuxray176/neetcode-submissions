class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        n = len(nums)
        res = float("-inf")

        for i in range(n):
            for j in range(n):
                if i == j:
                    continue
                for k in range(n):
                    if i == k or j == k:
                        continue
                    for l in range(n):
                        if i == l or j == l or k == l:
                            continue
                        res = max(res, (nums[i] * nums[j]) - nums[k] * nums[l])

        return res