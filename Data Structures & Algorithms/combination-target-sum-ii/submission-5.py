class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # res = []
        # path = []

        # def backtrack(start):
        #     res.append(path.copy())          # record every node, not just leaves
        #     for i in range(start, len(nums)):
        #         path.append(nums[i])          # choose
        #         backtrack(i + 1)              # explore
        #         path.pop()                    # un-choose
        
        # backtrack(0)
        # return res

        candidates.sort()

        res = []
        path = []

        def backtrack(start, curr_sum):
            if curr_sum == target:
                res.append(path.copy())
            if curr_sum > target:
                return
            
            for i in range(start, len(candidates)):
                if i > start and candidates[i-1] == candidates[i]:
                    continue
                
                path.append(candidates[i])
                backtrack(i+1, curr_sum + candidates[i])
                path.pop()

        backtrack(0,0)
        return res