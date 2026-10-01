class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        res = 0
        left, right = 0, n - 1

        while left < right:
            size = min(heights[left], heights[right]) * (right - left)
            res = max(res, size)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res