class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pairs = list(zip(position, speed))
        pairs.sort(reverse=True)

        stack = []

        for pos, spd in pairs:
            arriv_time = (target - pos) / spd

            while stack and arriv_time <= stack[-1]:
                stack.pop()

            stack.append(arriv_time)
            # print(stack)

        return len(stack)