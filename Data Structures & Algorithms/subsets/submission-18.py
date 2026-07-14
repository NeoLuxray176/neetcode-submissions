class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start):
            res.append(path.copy())          # record every node, not just leaves
            for i in range(start, len(nums)):
                path.append(nums[i])          # choose
                backtrack(i + 1)              # explore
                path.pop()                    # un-choose
        
        backtrack(0)
        return res