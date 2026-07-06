class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [nums]

        h = nums[0]
        currs = self.permute(nums[1:])

        res = []
        for curr in currs:
            for i in range(len(curr) + 1):
                mid = curr[:i] + [h] + curr[i:]
                res.append(mid)
        
        # print(res)
        return res