class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)

        stack = []

        for pos, spd in pairs:
            arriv_time = (target - pos) / spd
            stack.append(arriv_time)

            while len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

        return len(stack)