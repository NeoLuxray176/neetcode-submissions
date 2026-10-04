class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res, curr = 0, 0

        for num in nums:
            if num == 1:
                curr += 1
            else:
                curr = 0
            res = max(res, curr)

        return res