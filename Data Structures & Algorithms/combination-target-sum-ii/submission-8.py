class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()

        res = []


        def backtrack(path : List[int], candidates : List[int], curr_sum : int):
            if curr_sum > target:
                return
            if curr_sum == target:
                res.append(path)
                return

            if not candidates:
                return

            curr = candidates[0]
            backtrack(path + [curr], candidates[1:], curr_sum + curr)

            new_cands = [x for x in candidates if x != curr]
            backtrack(path, new_cands, curr_sum)

        backtrack([], candidates, 0)
        return res


            
