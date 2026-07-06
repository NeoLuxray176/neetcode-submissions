class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        h = [nums[0]]
        perms = self.permute(nums[1:])

        print(perms)

        res = []
        for perm in perms:
            for i in range(len(perm) + 1):
                curr = perm[:i] + h + perm[i:]
                res.append(curr)
        
        return res

