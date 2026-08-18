class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []

        def dfs(nums : List[int], history : List[int], target : int):
            if target == 0:
                res.append(history.copy())
                return

            if target < 0:
                return


            for i in range(len(nums)):
                num = nums[i]
                if target - num >= 0:
                    dfs(nums[i:], history + [num], target - num)


        dfs(nums, [], target)
        
        return res
                    