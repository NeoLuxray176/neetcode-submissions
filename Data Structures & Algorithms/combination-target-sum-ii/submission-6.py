class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # Decision tree
        # Choose or not choose a number, stop if we are above target
        # No repetitions of numbers
        # Backtracking style solution

        # Example [1, 2, 3, 1, 1] target 5
        # [1, 3, 1]
        # [3, 1, 1] # Not unique solution
        # [2, 3]
        # [1, 2, 1, 1]

        # Does this still happen if we sort the candidates?
        # Then we can process all '1's individually and handle the not choose a number case
        # such that we choose none of the subsequent '1's

        candidates.sort()

        res = []
        path = []

        def dfs(path : List[int], candidates : List[int], curr_sum : int):
            if curr_sum == target:
                res.append(path)
                return
            
            if curr_sum > target:
                return

            if not candidates:
                return

            cand = candidates[0]
            dfs(path + [cand], candidates[1:], curr_sum + cand)

            next_candidates = [x for x in candidates if x != cand]
            dfs(path, next_candidates, curr_sum)

            # for i in range(len(candidates)):
                # cand = candidates[i]
                # dfs(path + [cand], candidates[i+1:], curr_sum + cand)

                # next_candidates = [x for x in candidates[i:] if x != cand]
                # dfs(path, next_candidates, curr_sum)
            return

        dfs([], candidates, 0)
        return res