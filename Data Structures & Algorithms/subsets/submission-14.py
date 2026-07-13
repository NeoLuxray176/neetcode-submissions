class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            tmp = []
            for re in res:
                tmp.append(re + [num])
            res = res + tmp
        
        return res