class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # We start from the last position and calculate the time until the car arrives
        # A car belongs to the previous fleet if its arrival time is smaller or equal
        # to that of the previous car

        n = len(position)
        stack = []

        res = 0

        for i in range(n - 1, -1 , -1):
            arr_time = (target - position[i]) / speed[i]

            while stack and stack[-1] >= arr_time:
                stack.pop()

            # The stack now contains the arrival times of all cars
            # that will arrive later than the current car i.e. a car
            # that will be in the same fleet as the current car.
            # So if the stack is empty, we will have a new fleet

            if not stack:
                res += 1

            stack.append(arr_time)

        return res