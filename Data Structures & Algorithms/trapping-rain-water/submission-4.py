class Solution:
    def trap(self, height: List[int]) -> int:
        # The idea is that we use a two-pointer approach to calculate the amount of water that
        # is trapped.
        # Move from the two sides inwards until the two pointers point to the same index.
        # If the left side smaller than the right side then the amount of water that is trapped
        # is defined by the height of the left bar. (Otherwise water would spill out.)
        # Water is trapped on the left side if the maximum on the left side is larger than the
        # current block. We can use this fact to calculate the amount of water trapped in the
        # current block.
        n = len(height)
        left, right = 0, n - 1
        maxLeft, maxRight = height[left], height[right]
        
        res = 0

        while left < right:
            if height[left] < height[right]:
                maxLeft = max(maxLeft, height[left])
                res += maxLeft - height[left]
                left += 1
            else:
                maxRight = max(maxRight, height[right])
                res += maxRight - height[right]
                right -= 1

        return res

