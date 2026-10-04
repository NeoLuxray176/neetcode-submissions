class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 0, max(piles)

        res = max(piles)

        while left <= right:
            middle = (left + right) // 2

            if middle == 0:
                break

            curr = 0
            for pile in piles:
                curr += math.ceil(float(pile) / middle)
            
            if curr < h:
                res = min(res, middle)
                right = middle - 1
            else:
                left = middle + 1

        return res
