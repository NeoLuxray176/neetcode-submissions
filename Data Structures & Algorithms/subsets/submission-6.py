class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if not nums:
            return [[]]

        res = [[]]

        for num in nums:
            curr = []
            for curr_entry in res:
                mid = curr_entry + [num]
                curr.append(mid)
            res += curr
        
        print("currently", res)
        return res