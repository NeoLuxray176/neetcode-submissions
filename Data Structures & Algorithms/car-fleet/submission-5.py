class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [(p, s) for p, s in zip(position, speed)]
        pair.sort(reverse=True)

        n = len(position)
        stack = []

        fleets = 0

        print(position)
        print(speed)

        for i in range(n-1):
            curr_pos = pair[i][0]
            curr_speed = pair[i][1]

            j = i + 1
            next_pos = pair[j][0]
            next_speed = pair[j][1]

            if next_speed >= curr_speed:
                print(f"{i} cannot catch up, add to fleets")
                fleets += 1
                # continue
            else:
                dist_to_target = target - curr_pos
                dist_to_next = next_pos - curr_pos
                time_units_left_to_dist = dist_to_target / curr_speed
                time_units_left_to_next = dist_to_next / curr_speed

                print(f"{dist_to_target} / {curr_speed} {dist_to_next} / {curr_speed}")

                print(f"{i} will travel {time_units_left_to_dist} to dist;  next {time_units_left_to_next}")
                if time_units_left_to_dist <= time_units_left_to_next:
                    # They join the same fleet
                    print(f"{i} catches up and no new fleet will be created")
                    continue
                else:
                    print(f"{i} cannot catch up in the remaining time, add to fleets")
                    fleets += 1

        return fleets


