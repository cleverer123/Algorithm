class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if target < matrix[0][0]:
            return False
        m = len(matrix) - 1
        n = len(matrix[0]) - 1
        l, r = 0, m
        while l < r:
            if target <= (matrix[l][0] + matrix[r][0]) / 2:
                r -= 1 
            elif target > (matrix[l][0] + matrix[r][0]) / 2:
                l += 1
        
        if target < matrix[l][0]:
            l -= 1

        ll, rr = 0, n
        while ll <= rr:
            if target == matrix[l][ll]:
                return True
            elif target < (matrix[l][ll] + matrix[l][rr]) / 2:
                rr -= 1
            else:
                ll += 1
        return False

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
# matrix = [[1]]
target = 7

print(Solution().searchMatrix(matrix, target))