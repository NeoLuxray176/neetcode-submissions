class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # Task 
        # for each temperature find the number of days until a warmer temperature appears
        # if not warmer temperature occurs then we write a zero.

        # Constraints
        # All temperatures are positive
        # List has at least one element

        # General Idea
        # Brute Force
        # For each temperature go through all the future temperatures and check whether they are larger
        # Write the number of iterations it took us to a results array and return the array.
        # This is in O(n^2).

        # Can we do better?
        # We could go from the back and keep the temperatures in a stack.
        # As long as the temperatures are lower than the current temperature then we pop off the stack, once we find a warmer temperature
        # we know how many days it is until the that temperature. (We actually store the index not the temperature.)
        # Afterwards we add the current temperature on top of the stack, so the next result is always on the stack. Either because the current
        # temperature is higher or because we haven't popped the higher temperature off of the stack.

        n = len(temperatures)
        res = [0] * n
        stack = []

        for i in range(n - 1, -1, -1):
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                res[i] = stack[-1] - i
            stack.append(i)

        return res
