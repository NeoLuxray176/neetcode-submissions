class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        res = [0] * n
        stack = []

        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][1]:
                stack_ind, stack_temp = stack.pop()
                res[stack_ind] = i - stack_ind
            stack.append((i, temp))
        return res
