class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_val, max_val = 1, max(piles)
        res = max_val

        while min_val <= max_val:
            middle = (min_val + max_val) // 2
            duration = 0

            for pile in piles:
                duration += math.ceil(pile / middle)

            if duration > h:
                min_val = middle + 1
            else:
                res = middle
                max_val = middle - 1

        return res
