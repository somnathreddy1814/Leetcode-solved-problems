class Solution:
    def updateMatrix(self, grid: List[List[int]]) -> List[List[int]]:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        vis=[[0]*m for _ in range(n)]
        dist=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if grid[i][j]==0:
                    vis[i][j]=1
                    q.append(((i,j),0))
        delrow=[0,0,1,-1]
        delcol=[1,-1,0,0]
        while(q):
            (row,col),steps=q.popleft()
            dist[row][col]=steps
            for i in range(4):
                nrow=row+delrow[i]
                ncol=col+delcol[i]
                if 0<=nrow<n and 0<=ncol<m and grid[nrow][ncol]==1 and vis[nrow][ncol]==0:
                    vis[nrow][ncol]=1
                    q.append(((nrow,ncol),steps+1))
        return dist
        