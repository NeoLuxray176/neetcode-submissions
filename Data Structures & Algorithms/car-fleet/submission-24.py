class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for pos, spd in reversed(sorted(zip(position, speed))):
            arrival = (target - pos) / spd

            while stack and stack[-1] >= arrival:
                stack.pop()

            stack.append(arrival)

        return len(stack)