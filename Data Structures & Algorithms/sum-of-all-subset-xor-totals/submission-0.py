class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        n = len(nums)
        res = 0

        def dfs(start : int, subset : List[int]):
            nonlocal res
            xorr = 0
            for num in subset:
                xorr ^= num
            res += xorr

            for j in range(start, len(nums)):
                subset.append(nums[j])
                dfs(j + 1, subset)
                subset.pop()

        dfs(0, [])
        return res