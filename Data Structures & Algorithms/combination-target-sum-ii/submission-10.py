class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        def backtrack(path : List[int], curr_sum : int, index : int):
            if curr_sum == target:
                res.append(path[::])
                return
            
            if index >= len(candidates):
                return

            backtrack(path + [candidates[index]], curr_sum + candidates[index], index + 1)
            while index + 1 < len(candidates) and candidates[index] == candidates[index + 1]:
                index += 1
            backtrack(path, curr_sum, index + 1)

        backtrack([], 0, 0)
        return res