from collections import deque
class Solution:
    def bfs(self,grid,vis,q):
        def cnt(grid,vis):
            cntv=0
            for i in range(n):
                for j in range(m):
                    if grid[i][j]==1 and vis[i][j]==0:
                        cntv+=1
            return cntv
        
        
        n=len(grid)
        m=len(grid[0])
        delrow=[1,-1,0,0]
        delcol=[0,0,1,-1]
        if len(q)==0:
            return cnt(grid,vis)
        while(q):
            row,col=q.popleft()
            
            for i in range(4):
                nrow=row+delrow[i]
                ncol=col+delcol[i]
                if 0<=nrow<n and 0<=ncol<m and grid[nrow][ncol]==1 and vis[nrow][ncol]==0:
                    q.append((nrow,ncol))
                    vis[nrow][ncol]=1
        return cnt(grid,vis)
    
    def numEnclaves(self, grid: List[List[int]]) -> int:
        n=len(grid)
        m=len(grid[0])
        q=deque()
        vis=[[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if i==0 or i==n-1 or j==0 or j==m-1:
                    if grid[i][j]==1:
                        q.append((i,j))
                        vis[i][j]=1
        return self.bfs(grid,vis,q)
            
        