class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        stack = []

        fleets = 0

        for i in range(n-1):
            curr_pos = position[i]
            curr_speed = speed[i]

            j = i + 1
            next_pos = position[j]
            next_speed = speed[j]

            if next_speed >= curr_speed:
                fleets += 1
                continue
            else:
                dist_to_target = target - curr_pos
                dist_to_next = next_pos - curr_pos
                time_units_left_to_dist = dist_to_target / curr_speed
                time_units_left_to_next = dist_to_next / curr_speed

                if time_units_left_to_dist <= time_units_left_to_next:
                    # They join the same fleet
                    continue
                else:
                    fleets += 1

        return fleets


