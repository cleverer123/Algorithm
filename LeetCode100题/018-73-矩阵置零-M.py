class Solution:
    def setZeroes(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])
        mask = [[False] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                mask[i][j] = matrix[i][j] == 0

        for i in range(m):
            for j in range(n):            
                if mask[i][j] and matrix[i][j] == 0:
                    for r in range(m):
                        matrix[r][j] = 0
                    for c in range(n):
                        matrix[i][c] = 0                                 
        return matrix    

matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
print(Solution().setZeroes(matrix)) 