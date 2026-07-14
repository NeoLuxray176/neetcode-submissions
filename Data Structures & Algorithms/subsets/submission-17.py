class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        res = []

        stack = []

        def backtrack(i):
            if i >= n:
                res.append(stack.copy())
                return

            stack.append(nums[i])
            backtrack(i+1)

            stack.pop()
            backtrack(i+1)

        backtrack(0)
        return res