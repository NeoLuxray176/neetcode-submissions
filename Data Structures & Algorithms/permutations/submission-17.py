class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        res = [[]]
        
        for num in nums:
            new_perms = []
            for p in res:
                for i in range(len(p) + 1):
                    p_copy = p.copy()
                    p_copy.insert(i, num)
                    new_perms.append(p_copy)
            res = new_perms

        return res