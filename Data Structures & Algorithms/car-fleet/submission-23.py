class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = list(zip(position, speed))

        cars.sort(reverse=True)

        stack = []

        for pos, spd in cars:
            arrival_time = (target - pos) / spd
            stack.append(arrival_time)
            
            while len(stack) >= 2 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)