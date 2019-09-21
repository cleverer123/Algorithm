import numpy as np
from copy import deepcopy
class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        mark = [[0 for j in range(n)] for i in range(n)]
        location = [['.' for j in range(n)] for i in range(n)]

        def put_Queen(x, y, mark):            
            dx = [-1, -1, -1, 0, 0, 1, 1, 1]
            dy = [-1, 0, 1, -1, 1, -1, 0, 1]

            mark[x][y] = 1
            for i in range(1, n):        
                for j in range(8):
                    new_x = x + i * dx[j]
                    new_y = y + i * dy[j]
                    if new_x >=0 and new_x <len(mark) and new_y >= 0 and new_y < len(mark):
                        mark[new_x][new_y] = 1
            
        def back_tack(i, mark, location):

            if i == n:
                result.append(location)
                return 

            for j in range(n):               
                if mark[i][j] == 0:
                    tmp_mark = deepcopy(mark)
                    tmp_location = deepcopy(location)
                    put_Queen(i, j, mark)
                    location[i][j] = 'Q'
                    back_tack(i + 1, mark,  location)
                    mark = tmp_mark
                    location = tmp_location

        back_tack(0, mark, location)

        r = []
        for res in result:
            res = [''.join(line) for line in res]
            r.append(res)
        return r    
  
class Solution2:
    def solveNQueens(self, n):
        res = []
        def dfs(queens, xy_sum, xy_dif):
            i = len(queens)
            if i == n:
                res.append(queens)
                return 
            for j in range(n):
                if j not in queens and i + j not in xy_sum and i - j not in xy_dif:
                    dfs(queens + [j], xy_sum + [i + j], xy_dif + [i - j])

        dfs([], [], []) 

        return [["." * i + "Q" + "." * (n - i - 1) for i in sol] for sol in res]


if __name__ == '__main__':
   
    # s = 'abc'
    # s = s.replace('a', '.')
    # print(s)
    print(Solution2().solveNQueens( 4))


