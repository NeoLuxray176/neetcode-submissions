class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(list(zip(position, speed)), reverse=True)
        stack = []

        for pos, spd in cars:
            arr_time = (target - pos) / spd
            
            if not stack or arr_time > stack[-1]:
                stack.append(arr_time)

        return len(stack)
