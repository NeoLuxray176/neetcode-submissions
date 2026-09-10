class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)

        stack = []

        cars = list(zip(position, speed))
        cars.sort(reverse=True) # first car is now the car with the largest position

        for pos, spd in cars:
            arr = (target - pos) / spd

            stack.append(arr)

            while len(stack) >= 2 and stack[-2] >= stack[-1]:
                # There is a car with an arrival time larger than ours in front of us
                # this means we will catch up to him and therefore be in the same fleet
                stack.pop()

        return len(stack)