class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        
        left, right = 0, n * m - 1

        while left <= right:
            middle = (left + right) // 2
            i, j = middle // m, middle % m

            if target > matrix[i][j]:
                left = middle + 1
            elif target < matrix[i][j]:
                right = middle - 1
            else:
                return True

        return False