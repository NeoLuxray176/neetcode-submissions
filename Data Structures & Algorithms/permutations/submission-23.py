class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        if not nums:
            return [[]]


        curr = nums[0]
        prevs = self.permute(nums[1:])

        res = []
        for prev in prevs:
            for i in range(len(prev) + 1):
                res.append(prev[:i] + [curr] + prev[i:])

        print(res)
        return res