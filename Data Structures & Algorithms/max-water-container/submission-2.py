class Solution:
    # This is O(n)
    def maxArea(self, heights: List[int]) -> int:
        maximum_water = 0
        n = len(heights)
        i = 0
        j = n-1

        while i < j:
            left_height = heights[i]
            right_height = heights[j]
            
            curr_height = min(left_height, right_height)
            y_diff = j - i

            area = curr_height * y_diff
            maximum_water = max(maximum_water, area)

            if left_height > right_height:
                j -= 1
            else:
                i += 1
                
        
        return maximum_water

            