class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # We can view this as a decision tree
        # We tart out at the target and subtract each item from nums
        # or we don't. We are at a leaf if the number is <= 0
        # if it zero we have a valid result

        res = []

        def dfs(nums : List[int], history : List[int], target : int):
            if target == 0:
                res.append(history.copy())
                return

            if target < 0:
                return

            for i in range(len(nums)):
                if target - nums[i] >= 0:
                    dfs(nums[i:], history + [nums[i]], target - nums[i])

        
        dfs(nums, [], target)
        return res