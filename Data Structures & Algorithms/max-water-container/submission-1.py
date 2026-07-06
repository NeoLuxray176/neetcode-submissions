class Solution:
    # This is an O(n^2) solution
    def maxArea(self, heights: List[int]) -> int:
        maximum_water = 0
        n = len(heights)

        for i in range(n):
            for j in range(i,n):
                left_height = heights[i]
                right_height = heights[j]
                y_diff = j - i

                water = min(left_height, right_height) * y_diff

                if water > maximum_water:
                    maximum_water = water
        
        return maximum_water