class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        stack = []

        for pos, spd in cars:
            stack.append((target - pos) / spd)

            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)