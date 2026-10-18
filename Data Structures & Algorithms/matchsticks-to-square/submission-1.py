class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        # Task: Create a square from matchsticks
        # each matchstick must be used exactly once
        # Constraints: up to 15 matchsticks length is up to 100,000,000
        # General Idea:
        # A square has four sides of equal length, we must use each matchstick exactly once
        # We must partition the matchsticks into four groups of equal size.
        # It is not enough to check whether we can fulfill sum / 4.
        # Refined Idea:
        # Explore all paths, have four lists of numbers. Once we've used all sticks, check if their
        # length is equal. This is 4^n
        # Test Vectors:

        if sum(matchsticks) % 4 != 0:
            return False

        n = len(matchsticks)
        s = sum(matchsticks)
        # square = [0, 0, 0, 0]

        def backtrack(start : int, square : List[int]) -> bool:
            for i in range(4):
                if square[i] > s // 4:
                    return False
            if start == n:
                return square[0] == square[1] == square[2] == square[3]

            for i in range(4):
                square[i] += matchsticks[start]
                if backtrack(start + 1, square):
                    return True
                square[i] -= matchsticks[start]

            return False

        return backtrack(0, [0, 0, 0, 0])

