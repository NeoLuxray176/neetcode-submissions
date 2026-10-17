class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)

        def recurse(curr_length : int, start : int):
            if start >= n:
                return curr_length

            res = curr_length
            for j in range(start + 1, n):
                if nums[j] > nums[start]:
                    res = max(res, recurse(curr_length + 1, j))

            return res

        res = 1
        for i in range(n):
            res = max(res, recurse(1, i))

        return res

