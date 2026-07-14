class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return []
        if len(nums) < 2:
            return [nums]
        
        res = [[]]

        for num in nums:
            tmp = []
            for re in res:
                for i in range(len(re) + 1):
                    mid = re.copy()
                    mid.insert(i, num)
                    tmp.append(mid)
            
            res = tmp

        print(res)
        return res