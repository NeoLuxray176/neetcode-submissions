class Solution:
    def climbStairs(self, n: int) -> int:
        # For each step, calculate the number of ways that we can reach it
        # For the first step this is one way
        # 2. two ways
        # 3. three ways (1 + 2, 2 + 1, 1 + 1 + 1)


        if n == 0:
            return 0
        if n == 1:
            return 1
        if n == 2:
            return 2

        dp = [0] * (n)

        dp[0] = 1
        dp[1] = 2

        for i in range(2, n):
            dp[i] = dp[i - 2] + dp[i - 1]

        return dp[-1]
