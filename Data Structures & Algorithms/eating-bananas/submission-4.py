class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_val = 1
        max_val = max(piles)
        old_duration = -1
        its = 0

        while min_val <= max_val:
            its += 1
            middle = (min_val + max_val) // 2

            # if middle == 0:
                # return 1
            
            duration = 0
            for pile in piles:
                time_to_eat = math.ceil(pile / middle)
                duration += time_to_eat
            
            if duration > h:
                min_val = middle + 1
            elif duration <= h:
                max_val = middle - 1
            
            print(f"{old_duration} {middle}")
            if old_duration == middle:
                return min_val
            old_duration = middle
        
        return -1 



        
