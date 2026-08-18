class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        # for x in nums:
            # res += [subset + [x] for subset in res]

        for num in nums:
            tmp = []
            for re in res:
                tmp.append(re + [num])
            
            res += tmp

        print(res)
        return res