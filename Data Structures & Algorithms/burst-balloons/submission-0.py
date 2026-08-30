class Solution:
    def maxCoins(self, nums: List[int]) -> int:
        # Pad both ends with virtual balloons of value 1.
        # This lets boundary balloons be burst using a valid triplet product.
        nums = [1] + nums + [1]

        def dfs(nums : List[int]):
            n = len(nums)

            # Base case: only the two boundary balloons remain, nothing left to burst.
            if n == 2:
                return 0

            maxCoins = 0
            # Try every possible balloon to burst LAST within this sub-list
            # (i.e., i is the last one popped among nums[1:-1]).
            for i in range(1, n - 1):
                # Coins earned by bursting nums[i] last: its neighbors at
                # burst-time are the current boundaries nums[i-1] and nums[i+1].
                coins = nums[i - 1] * nums[i] * nums[i + 1]

                # Recurse on the sub-list with nums[i] removed, since it's
                # already "burst" — the remaining balloons must still be
                # cleared, with i's former neighbors now adjacent.
                coins += dfs(nums[:i] + nums[i + 1:])

                # Track the best total across all choices of i.
                maxCoins = max(maxCoins, coins)

            return maxCoins

        return dfs(nums)