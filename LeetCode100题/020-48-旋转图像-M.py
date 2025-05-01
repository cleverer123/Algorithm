class Solution:
    # 方法一：旋转交换 
    def rotate(self, matrix ) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        m, n = len(matrix), len(matrix[0])
        for i in range(m // 2):
            for j in range((n + 1)// 2):
                matrix[i][j], matrix[j][m - 1 - i], matrix[m - 1 - i][n - 1 - j], matrix[n - 1 - j][i] = \
                matrix[n - 1 - j][i], matrix[i][j], matrix[j][m - 1 - i], matrix[m - 1 - i][n - 1 - j]
    
    # 方法二：翻转交换，先水平翻转，再沿主对角线翻转
    def rotate(self, matrix) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        for i in range(n // 2):
            for j in range(n):
                matrix[n - 1 - i][j], matrix[i][j] = matrix[i][j], matrix[n - 1 - i][j]
        
        for i in range(n):
            for j in range(0, i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            