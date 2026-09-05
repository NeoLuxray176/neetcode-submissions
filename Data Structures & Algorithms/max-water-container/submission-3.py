class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        
        res = 0

        left, right = 0, n - 1 

        while left <= right:
            n, m = min(heights[left], heights[right]), right - left
            curr_res = n * m
            res = max(curr_res, res)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res