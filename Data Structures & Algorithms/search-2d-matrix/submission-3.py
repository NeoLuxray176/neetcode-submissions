class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix[0]), len(matrix)
        row_left, row_right = 0, n - 1
        col_left, col_right = 0, m - 1

        while row_left <= row_right:
            middle = (row_left + row_right) // 2

            if matrix[middle][0] <= target and matrix[middle][-1] >= target:
                break
            elif matrix[middle][-1] < target:
                row_left = middle + 1
            elif matrix[middle][0] > target:
                row_right = middle - 1
        
        row = (row_left + row_right) // 2
        
        while col_left <= col_right:
            middle = (col_left + col_right) // 2

            if matrix[row][middle] == target:
                return True
            elif matrix[row][middle] <= target:
                col_left = middle + 1
            else:
                col_right = middle - 1

        return False
        