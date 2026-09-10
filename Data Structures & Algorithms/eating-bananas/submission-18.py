class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # We do a binary search on the possible
        # eating speeds.
        # Start with 1 and the maximum speed i.e. the size of the largest pile

        left, right = 1, max(piles)
        res = 0

        while left <= right:
            middle = (left + right) // 2

            curr = 0
            for pile in piles:
                curr += math.ceil(pile / middle)

            if curr <= h:
                res = middle
                right = middle - 1
            else:
                left = middle + 1

        return res