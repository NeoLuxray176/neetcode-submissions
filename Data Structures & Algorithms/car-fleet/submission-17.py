class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Here we use a monotonic stack with a slight twist
        # We add cars to the stack and then pop all of them off until we find one
        # that arrives earlier than we do.
        # This way we have one car per car fleet and we can return the length of the stack

        stack = []

        cars = list(zip(position, speed))
        cars.sort(reverse=True)

        for pos, speed in cars:
            stack.append((target - pos) / speed)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()

            

        return len(stack)