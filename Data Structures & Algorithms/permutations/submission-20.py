class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)

        if n == 0:
            return [[]]

        curr = nums[0]
        remain = nums[1:]
        perms = self.permute(remain)
        res = []

        for perm in perms:
            for i in range(len(perm) + 1):
                res.append(perm[i:] + [curr] + perm[:i])

        return res