class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            tmp = []
            for p in res:
               for i in range(len(p) + 1):
                p_copy = p.copy()
                p_copy.insert(i, num)
                tmp.append(p_copy) 

            res = tmp

        return res