class Solution:
    # 以右上角为根节点看成二叉搜索树，比target大，往左，比target小，往右。
    def searchMatrix(self, matrix , target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        row, col = 0, n - 1
        while True:
            if row < 0 or row >=m or col < 0 or col >=n:
                return False
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                row += 1
            else:
                col -= 1