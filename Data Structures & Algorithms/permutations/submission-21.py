class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            tmp = []
            for re in res:
                for i in range(len(re) + 1):
                    rep = re.copy()
                    rep.insert(i, num)
                    tmp.append(rep)

            res = tmp

        return res