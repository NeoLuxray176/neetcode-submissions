class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])

        left, right = 0, n - 1
        middle_row = (left + right) // 2

        while left <= right:
            middle_row = (left + right) // 2

            if matrix[middle_row][0] <= target and matrix[middle_row][-1] >= target:
                break
            elif matrix[middle_row][0] < target:
                left = middle_row + 1
            else:
                right = middle_row - 1

        
        left, right = 0, m - 1
        while left <= right:
            middle_col = (left + right) // 2

            if matrix[middle_row][middle_col] == target:
                return True
            elif matrix[middle_row][middle_col] < target:
                left = middle_col + 1
            else:
                right = middle_col - 1

        return False

            