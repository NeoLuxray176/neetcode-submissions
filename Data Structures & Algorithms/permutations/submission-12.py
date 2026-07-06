class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            curr = []
            for re in res:
                for i in range(len(re) + 1):
                    mid = re.copy()
                    mid.insert(i, num)
                    curr.append(mid)
            res = curr
        
        return res