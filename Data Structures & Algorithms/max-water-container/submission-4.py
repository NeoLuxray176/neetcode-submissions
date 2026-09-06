class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1
        res = 0

        while left < right:
            curr_height = min(heights[left], heights[right])
            cand_res = curr_height * (right - left)
            res = max(res, cand_res)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res