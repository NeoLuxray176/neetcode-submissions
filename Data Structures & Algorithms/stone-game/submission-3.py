from functools import cache

class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        # Here is the key insight: with an even number of piles and an odd total sum, Alice can always win. 
        # She can always choose to take all even-indexed piles or all odd-indexed piles. 
        # Since the total is odd, one of these sets must have a larger sum. 
        # Alice, moving first, can force the game to give her whichever set she prefers, guaranteeing a win.
        return True


            