class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        if len(grid) == 0:
            return 0
        rows = len(grid)
        cols = len(grid[0])
        mark = [[0 for _ in range(cols)] for _ in range(rows) ] 

        island = 0

        dx = [-1, 1, 0, 0]
        dy = [0, 0, -1, 1]

        def dfs(x, y):
            mark[x][y] = 1
            for i in range(4):

                new_x = dx[i] + x
                new_y = dy[i] + y
                if new_x < 0 or new_x >= len(mark) or new_y < 0 or new_y >= len(mark):
                    continue
                if mark[new_x][new_y] == 0 and grid[new_x][new_y] == '1':
                    dfs(new_x, new_y)
                
        
        def bfs(x, y):
            queue = [[x, y]]
            mark[x][y] = 1
            while len(queue) > 0:
                front = queue.pop(0)
                x = front[0]
                y = front[1]
                
                for i in range(4):
                    new_x = dx[i] + x
                    new_y = dy[i] + y
                    if new_x < 0 or new_x >= len(mark) or new_y < 0 or new_y >= len(mark[0]):
                        continue
                    if grid[new_x][new_y] == '1' and mark[new_x][new_y] == 0 :
                        queue.append([new_x, new_y])
                        mark[new_x][new_y] = 1
                
        for x in range(rows):
            for y in range(cols):
                if mark[x][y] == 0 and grid[x][y] == '1':
                    bfs(x, y)
                    island += 1
        
        return island

if __name__ == "__main__":
    # s1 = '11110'
    # s2 = '11010'
    # s3 = '11000'
    # s4 = '00000'
    # grid = []
    # grid.append(list(s1))
    # grid.append(list(s2))
    # grid.append(list(s3))
    # grid.append(list(s4))


    grid = [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]]

    print(Solution().numIslands(grid))
    


