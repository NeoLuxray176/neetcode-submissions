class Solution:
    def trap(self, height: List[int]) -> int:
        # Rain water is trapped with the maximum value from the left (or right) side
        # and the current height of the bar

        n = len(height)
        left, right = 0, n - 1
        maxLeft, maxRight = height[left], height[right]

        res = 0


        while left <= right:
            if height[left] < height[right]:
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]
                right -= 1

        return res
