from collections import deque

class Solution:

    # Function to find minimum time required to rot all oranges. 
    def bfs(self, grid, q, cnt_fresh):
        n = len(grid)
        m = len(grid[0])
        cnt = 0
        min_time = 0
        del_col = [0, 0, -1, 1]
        del_row = [1, -1, 0, 0]
        while q:
            size = len(q)
            
            for _ in range(size):
                row, col = q.popleft()
                for i in range(4):
                    nrow = row + del_row[i]
                    ncol = col + del_col[i]
                    if 0 <= nrow < n and 0 <= ncol < m and grid[nrow][ncol] == 1:
                        grid[nrow][ncol] = 2
                        cnt+=1
                        q.append((nrow, ncol))
            if q:
                min_time += 1
        if cnt != cnt_fresh:
            return -1
        return min_time
    
    def orangesRotting(self, grid):
        # Code here
        n = len(grid)
        m = len(grid[0])
        cnt_fresh = 0
        q = deque()
        if n == 0 or grid is None:
            return 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == 1:
                    cnt_fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))
        if cnt_fresh == 0:
            return 0
        return self.bfs(grid, q, cnt_fresh)