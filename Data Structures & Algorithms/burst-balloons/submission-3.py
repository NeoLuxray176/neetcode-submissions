class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad both ends with virtual balloons of value 1,
        # so boundary balloons still have valid neighbors to multiply with.
        nums = [1] + nums + [1]

        # Memoization cache: dp[(l, r)] = max coins obtainable from
        # bursting all balloons in the open interval (l, r) — i.e.
        # nums[l..r] inclusive — treating nums[l-1] and nums[r+1] as fixed.
        dp = {}

        def dfs(l : int, r : int):
            # Empty interval: nothing to burst, no coins.
            if l > r:
                return 0

            # Return cached result if this interval was already solved.
            if (l, r) in dp:
                return dp[(l, r)]

            dp[(l, r)] = 0
            # Choose i as the balloon burst LAST within (l, r).
            # Its neighbors at burst-time are the interval's fixed
            # boundaries nums[l-1] and nums[r+1], since everything
            # else in (l, r) has already been cleared by then.
            for i in range(l, r + 1):
                coins = nums[l - 1] * nums[i] * nums[r + 1]

                # Recurse on the two independent sub-intervals split by i:
                # everything left of i, and everything right of i.
                coins += dfs(l, i - 1) + dfs(i + 1, r)

                # Keep the best choice of "last balloon" for this interval.
                dp[(l, r)] = max(dp[(l, r)], coins)

            return dp[(l, r)]

        # Solve for the full original range, excluding the two padding balloons.
        return dfs(1, len(nums) - 2)