class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        left = 0
        right = len(matrix) - 1 # This is m

        while left < right:
            middle = (left + right) // 2
            curr_val = matrix[middle][0]

            if curr_val == target:
                return True
            elif curr_val < target:
                left = middle + 1
            else: # curr_val > target
                right = middle - 1

        middle = (left + right) // 2
        curr_row = matrix[middle]

        print(f"Identified row {middle} {curr_row}")

        left = 0
        right = len(curr_row) - 1

        while left <= right:
            middle = (left + right) // 2
            curr_val = curr_row[middle]

            if curr_val == target:
                return True
            elif curr_val < target:
                left = middle + 1
            else: # curr_val > target
                right = middle - 1

        return False


        