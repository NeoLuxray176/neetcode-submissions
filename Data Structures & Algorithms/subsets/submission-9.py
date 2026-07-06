class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]

        for num in nums:
            curr = []
            for curr_entry in res:
                mid = curr_entry + [num]
                curr.append(mid)
            res += curr

        return res