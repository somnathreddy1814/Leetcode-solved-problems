class Solution:              
    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        n=len(land)
        m=len(land[0])
        res=[]
        drow=[1,-1,0,0]
        dcol=[0,0,1,-1]
        vis=[[0]*m for _ in range(n)]
        def bfs(start_row,start_col):
            vis[start_row][start_col]=1
            q=deque()
            q.append((start_row,start_col))
            drow=[1,-1,0,0]
            dcol=[0,0,1,-1]
            min_row, min_col, max_row, max_col = start_row, start_col, start_row, start_col
            while(q):
                cur_row,cur_col=q.popleft()
                for i in range(4):
                    new_row=cur_row+drow[i]
                    new_col=cur_col+dcol[i]
                    if new_row>=0 and new_row<n and new_col>=0 and new_col<m and vis[new_row][new_col]==0 and land[new_row][new_col]==1:
                        vis[new_row][new_col]=1
                        q.append((new_row,new_col))
                        min_row=min(min_row,new_row)
                        min_col=min(min_col,new_col)
                        max_row=max(max_row,new_row)
                        max_col=max(max_col,new_col)
            return [min_row,min_col,max_row,max_col]
        for i in range(n):
            for j in range(m):
                if land[i][j]==1 and vis[i][j]==0:
                    farm=bfs(i,j)
                    res.append(farm)
        return res
