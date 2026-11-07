class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        one = nums[0]
        rems = self.permute(nums[1:])
        res = []

        for rem in rems:
            for i in range(len(rem) + 1):
                res.append(rem[:i] + [one] + rem[i:])

        return res
