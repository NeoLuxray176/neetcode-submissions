class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            curr = []
            for re in res:
                curr += [re + [num]]
            res += curr
        
        return res