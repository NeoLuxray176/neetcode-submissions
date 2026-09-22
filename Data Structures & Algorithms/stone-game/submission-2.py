from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # General Idea
        # Simulation, we simulate the turns and each player always makes the optimal choice
        # i.e. picks the largest stone.
        # Now is picking the largest stone even the optimal choice?
        # No because we need to consider the case where choosing the largest stone unlocks 
        # an even larger stone for the other player
        # Consider the game [1, 2, 100, 3]. Choosing three for alice would lead to a loss.
        # We need to enumerate all cases instead.

        @cache
        def dfs(i : int, j : int) -> int: # return the best result for alice
            if i > j:
                return 0

            even = (j - i) % 2 == 0
            left = piles[i] if even else 0
            right = piles[j] if even else 0

            res = max(dfs(i + 1, j) + left, dfs(i, j - 1) + right)
            return res

        res = dfs(0, len(piles) - 1)
        
        if sum(piles) - res > res:
            return False
        return True

            