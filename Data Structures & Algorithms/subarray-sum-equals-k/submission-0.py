class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n = len(nums)
        res = 0

        for i in range(n):
            total = 0
            for j in range(i, n):
                total += nums[j]
                if total == k:
                    res += 1

        return res


        

