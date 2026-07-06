class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            curr = []
            for re in res:
                arr = re.copy()
                arr.append(num)
                curr.append(arr)
            res += curr
        
        return res
