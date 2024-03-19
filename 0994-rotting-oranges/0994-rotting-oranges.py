class Solution:
    def bfs(self,grid, queue, count_fresh):
        rows, cols = len(grid), len(grid[0])
        countMin = 0
        cnt = 0
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]

        while queue:
            size = len(queue)
            cnt += size
            for _ in range(size):
                point = queue.popleft()
                for j in range(4):
                    x = point[0] + dx[j]
                    y = point[1] + dy[j]

                    if x < 0 or y < 0 or x >= rows or y >= cols or grid[x][y] == 0 or grid[x][y] == 2:
                        continue

                    grid[x][y] = 2
                    queue.append((x, y))
            if queue:
                countMin += 1

        return countMin if count_fresh == cnt else -1
    def orangesRotting(self, grid: List[List[int]]) -> int:

        if grid is None or len(grid) == 0:
            return 0
        rows, cols = len(grid), len(grid[0])
        queue = deque()
        count_fresh = 0

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] != 0:
                    count_fresh += 1

        if count_fresh == 0:
            return 0

        return self.bfs(grid, queue, count_fresh)
