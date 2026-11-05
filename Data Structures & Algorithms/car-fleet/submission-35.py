class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = zip(position, speed)

        fleets = []

        for pos, spd in cars:
            arr_time = (target - pos) / spd

            fleets.append(arr_time)

            while len(fleets) > 1 and fleets[-2] >= fleets[-1]:
                fleets.pop()

        return len(fleets)
        