class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0:
            return []

        if len(nums) == 1:
            return [nums]

        curr = nums[0]
        perms = self.permute(nums[1:])
        res = []
        for perm in perms:
            for i in range(len(perm) + 1):
                res.append(perm[:i] + [curr] + perm[i:])
        
        return res
