class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
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

        res = []
        path = []

        def backtrack(start, curr_sum):
            if curr_sum == target:
                res.append(path.copy())
                return
            
            if curr_sum > target:
                return

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i, curr_sum + nums[i])
                path.pop()

        backtrack(0, 0)
        return res