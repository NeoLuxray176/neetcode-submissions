class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []

        for pos, spd in sorted(zip(position, speed), reverse=True):
            arr_time = (target - pos) / spd
            stack.append(arr_time)

            while len(stack) > 1 and stack[-2] >= stack[-1]:
                stack.pop()

        return len(stack)