class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles)

        res = 0

        while left <= right:
            middle = (left + right) // 2

            curr = 0
            for pile in piles:
                curr += math.ceil(pile / middle)

            if curr > h:
                left = middle + 1
            else:
                res = middle
                right = middle - 1

        return res