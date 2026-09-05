class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        stack = []

        leftMost = [-1] * n # Smaller than the minimum index value we can have
        for i in range(n):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                leftMost[i] = stack[-1]
            stack.append(i)

        stack = []
        rightMost = [n] * n # Larger than the maximum index value we can have
        for i in range(n - 1, -1, -1):
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()
            if stack:
                rightMost[i] = stack[-1]
            stack.append(i)

        res = 0
        for i in range(n):
            # We store the index of the next bar that we cannot use for the
            # rectangle, so we have to adjust the indices by moving them to the right for the
            # left rectangles and to the right for the right rectangles
            leftMost[i] += 1
            rightMost[i] -= 1
            curr_area = heights[i] * (rightMost[i] - leftMost[i] + 1)
            res = max(res, curr_area)
        return res