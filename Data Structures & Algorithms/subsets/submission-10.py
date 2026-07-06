class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            iteration = []
            for re in res:
                curr = re.copy()
                curr.append(num)
                iteration.append(curr)
            res += (iteration)
        
        print(res)
        return res