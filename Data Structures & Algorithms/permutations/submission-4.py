class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            temp = []
            for re in res:
                for i in range(len(re) + 1):
                    curr = re.copy()
                    curr.insert(i, num)
                    temp.append(curr)
            res = temp

        return res
