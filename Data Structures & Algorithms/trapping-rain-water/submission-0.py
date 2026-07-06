class Solution:
    def trap(self, height: List[int]) -> int:
        l = 0
        r = len(height) - 1
        total_water = 0
        
        left_max = height[l]
        right_max = height[r]

        while l < r:
            if left_max < right_max:
                l += 1
                left_max = max(left_max, height[l])
                total_water += left_max - height[l]
            else:
                r -= 1
                right_max = max(right_max, height[r])
                total_water += right_max - height[r]
        
        return total_water
