class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []

        def backtrack(i : int, path : List[int]):
            if i >= len(nums):
                res.append(path.copy())
                return
            
            

            j = i + 1
            backtrack(j, path + [nums[i]])
            while j < len(nums) and nums[j] == nums[i]:
                j += 1  
            backtrack(j, path)
            return

        backtrack(0, [])

        return res
        