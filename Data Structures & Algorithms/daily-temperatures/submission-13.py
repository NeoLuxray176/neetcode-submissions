class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        
        stack = []
        res = [0] * n

        for i  in range(n - 1, -1, -1):
            temperature = temperatures[i]

            while stack and temperatures[stack[-1]] <= temperature:
                stack.pop()

            if stack:
                res[i] = stack[-1] - i
            
            stack.append(i)

        return res