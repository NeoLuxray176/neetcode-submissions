class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        n = len(candidates)

        res = []

        def backtrack(path : List[int], cands : List[int], curr_sum):
            if curr_sum == target:
                res.append(path[::])
                return

            if curr_sum > target:
                return

            for i in range(len(cands)):
                if i > 0 and cands[i - 1] == cands[i]:
                    continue

                path.append(cands[i])
                backtrack(path, cands[i + 1:], curr_sum + cands[i])
                path.pop()

        backtrack([], candidates, 0)
        return res