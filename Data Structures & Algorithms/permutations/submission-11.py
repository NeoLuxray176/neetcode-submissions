class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        
        h = nums[0]
        currs = self.permute(nums[1:])

        res = []

        for curr in currs:
            for i in range(len(curr) + 1):
                mid = curr[:i] + [h] + curr[i:]
                res.append(mid)
        
        return res