from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def bfs(row,col,vis,grid):
            q=deque()
            n=len(grid)
            m=len(grid[0])
            vis[row][col]=1
            q.append((row,col))
            while(q):
                row,col=q.popleft()
                delrow=[-1,0,1,0]
                delcol=[0,-1,0,+1]
                for i in range(4):
                    nrow=delrow[i]+row
                    ncol=delcol[i]+col
                    if 0<=nrow<n and 0<=ncol<m and vis[nrow][ncol]==0 and grid[nrow][ncol]=='1':
                        vis[nrow][ncol]=1
                        q.append((nrow,ncol))
                        
        
        
        n=len(grid)
        m=len(grid[0])
        vis=[[0]*m for _ in range(n)]
        cnt=0
        for i in range(n):
            for j in range(m):
                if vis[i][j]==0 and grid[i][j]=='1':
                    cnt+=1
                    bfs(i,j,vis,grid)
        return cnt
        