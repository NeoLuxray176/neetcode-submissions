class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []

        def backtrack(path : List[int], curr_candidates : List[int], curr_sum : int):
            if curr_sum == target:
                res.append(path[::])
                return

            for i in range(len(curr_candidates)):
                if i > 0 and curr_candidates[i - 1] == curr_candidates[i]:
                    continue
                if curr_sum + curr_candidates[i] > target:
                    break
                
                path.append(curr_candidates[i])
                backtrack(path, curr_candidates[i + 1:], curr_sum + curr_candidates[i])
                path.pop()

        backtrack([], candidates, 0)

        return res
