class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]
        
        num = nums[0]
        res = self.subsets(nums[1:])

        curr = []
        for re in res:
            curr.append(re + [num])
        
        res += curr

        return res
        