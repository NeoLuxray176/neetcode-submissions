class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        
        h = nums[0]
        res = self.permute(nums[1:])

        tmp = []
        for re in res:
            for i in range(len(re) + 1):
               tmp.append(re[:i] + [h] + re[i:])
        return tmp