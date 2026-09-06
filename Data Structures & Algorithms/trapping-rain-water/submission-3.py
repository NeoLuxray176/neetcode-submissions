class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0

        n = len(height)
        left, right = 0, n - 1
        left_max, right_max = height[left], height[right]
        
        res = 0
        
        while left < right:
            if left_max < right_max:
                # Since the left wall is smaller than the right wall
                # the water level at the current `left` position is
                # the left_max minus the height at the current position.
                # Remember rain water is also stored if the current height is smaller
                # than both left and right. This is encoded in the max() expression,
                # because if the current height is smaller than left_max then we take left_max
                # and subtract it from itself.
                left += 1
                left_max = max(left_max, height[left])
                res += left_max - height[left]
            else:
                right -= 1
                right_max = max(right_max, height[right])
                res += right_max - height[right]

        return res