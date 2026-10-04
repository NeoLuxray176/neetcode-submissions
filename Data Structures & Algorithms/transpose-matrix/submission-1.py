class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        n, m = len(matrix), len(matrix[0])
        new = [[-1] * n for _ in range(m)]

        for i in range(n):
            for j in range(m):
                new[j][i] = matrix[i][j]

        return new
