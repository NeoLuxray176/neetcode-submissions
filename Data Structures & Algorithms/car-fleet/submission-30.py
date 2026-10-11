class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), reverse=True)
        stack = []

        for pos, spd in cars:
            arr_time = (target - pos) / spd
            
            while stack and stack[-1] >= arr_time:
                stack.pop()

            stack.append(arr_time)

        return len(stack)
