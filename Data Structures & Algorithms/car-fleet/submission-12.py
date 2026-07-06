class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = [(p, s) for p, s in zip(position, speed)]
        pairs.sort(reverse=True)

        fleets = 1

        prev_time = (target - pairs[0][0]) / pairs[0][1]

        for curr_pos, curr_speed in pairs:
            curr_time = (target - curr_pos) / curr_speed
            if curr_time > prev_time:
                fleets += 1
                prev_time = curr_time
        return fleets


