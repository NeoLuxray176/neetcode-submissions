class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0]) # row, cols
        left, right = 0, n * m - 1

        while left <= right:
            middle = (left + right) // 2

            # We find the row by dividing the index by the number of rows
            # We find the column by taking the remainder (a full row )
            i, j = middle // m, middle % m

            if matrix[i][j] == target:
                return True
            elif matrix[i][j] < target:
                left = middle + 1
            else:
                right = middle - 1

        return False