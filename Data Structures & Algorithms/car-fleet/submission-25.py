class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Task:
        # Calculate the number of car fleets
        # A fleet consists of one or more cars that arrive at the same time
        # Two cars arrive at the same time if they have same start position and speed
        # or a car has a closer start position or higher speed and catches up to an earlier car.

        # Constraints:
        # All cars positioned correctly i.e. before target
        # What happens if multiple cars have the same start position? Nothing, start positions are unique
        
        # General Idea:
        # Sort cars by position, closest to target (i.e. largest position first)
        # Iterate over the cars and calculate the arrival time
        # In a stack we keep all cars that arrived earlier than we did, we pop cars that would've arrived later
        # i.e. cars that would be in the same fleet as we.

        cars = list(zip(position, speed))
        cars.sort(reverse=True)
        stack = []

        for pos, spd in cars:
            arr_time = (target - pos) / spd

            while stack and stack[-1] >= arr_time:
                stack.pop()

            stack.append(arr_time)

        return len(stack)
