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

        def dfs(i : int, j : int, alice_sum : int, alices_turn : bool) -> int: # return the best result for alice
            if i == j:
                return alice_sum

            if alices_turn:
                a = dfs(i + 1, j, alice_sum + piles[i], False)
                b = dfs(i, j - 1, alice_sum + piles[j], False)
                return max(a, b)
            else:
                a = dfs(i + 1, j, alice_sum, True)
                b = dfs(i, j - 1, alice_sum, True)
                return min(a, b)

        res = dfs(0, len(piles) - 1, 0, True)
        
        if sum(piles) - res > res:
            return False
        return True

            