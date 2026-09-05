class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n

        # Stack holds INDICES (not temperatures), kept in strictly
        # decreasing order of temperature from bottom to top.
        # This lets us recover the true distance (stack_index - i)
        # instead of inferring it from how many elements we popped.
        stack = []

        for i in range(n - 1, -1, -1):
            # Pop every index whose temperature is <= today's temperature:
            # those days are not warmer than today, so they can never be
            # the answer for any day to the left of i either (today is
            # always a better/equal candidate for future comparisons).
            while stack and temperatures[stack[-1]] <= temperatures[i]:
                stack.pop()

            if stack:
                # Top of stack is now the nearest index to the right
                # with a strictly greater temperature.
                res[i] = stack[-1] - i
            # else: no warmer day ahead, res[i] stays 0

            stack.append(i)

        return res