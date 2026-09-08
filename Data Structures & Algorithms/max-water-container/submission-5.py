class Solution:
    def maxArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = 0, n - 1

        res = 0

        # print(f"[{left},{right}] {res}")

        while left <= right:
            new_area = (right - left) * min(heights[left], heights[right])
            # print(f"[{left},{right}] {new_area}")
            res = max(res, new_area)

            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1

        return res