class Solution:
    def bfs(self,grid, q, count_fresh):
        n, m = len(grid), len(grid[0])
        countMin = 0
        cnt = 0
        delrow = [1,-1,0,0]
        delcol = [0,0,-1,1]

        while q:
            size = len(q)
            cnt += size
            for _ in range(size):
                row,col = q.popleft()
                for i in range(4):
                    nrow = row + delrow[i]
                    ncol = col + delcol[i]

                    if nrow < 0 or ncol < 0 or nrow >= n or ncol >= m or grid[nrow][ncol] == 0 or grid[nrow][ncol] == 2:
                        continue

                    grid[nrow][ncol] = 2
                    q.append((nrow, ncol))
            if q:
                countMin += 1

        return countMin if count_fresh == cnt else -1
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if grid is None or len(grid) == 0:
            return 0
        n, m = len(grid), len(grid[0])
        q = deque()
        count_fresh = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] == 2:
                    q.append((i, j))
                if grid[i][j] != 0:
                    count_fresh += 1

        if count_fresh == 0:
            return 0

        return self.bfs(grid, q, count_fresh)
