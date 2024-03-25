from collections import deque
class Solution:

    #Function to find minimum time required to rot all oranges. 
	def orangesRotting(self, grid):
		#Code here
		def bfs(grid,q,cnt_fresh):
		    n=len(grid)
		    m=len(grid[0])
		    cnt=0  #to check if all oranges marked fresh are touched or not
		    min=0  #count of minutes to return 
		    delrow=[1,-1,0,0]#as we can move in 4 directons these are possible changes
		    delcol=[0,0,1,-1]
		    while(q):
		        for _ in range(len(q)):
		            row,col=q[0][0]
		            t=q[0][1]
		            for i in range(4):
		                nrow=row+delrow[i]
		                ncol=col+delcol[i]
		                if 0<=nrow<n and 0<=ncol<m and grid[nrow][ncol]==1:
		                    cnt+=1
		                    grid[nrow][ncol]=2 #modify neigbours
		                  
		                    q.append(((nrow,ncol),t+1)) #append locations to queue to explore those as well
		        q.popleft()
		                
		        if q:
		            min+=1 #update levels
		    if cnt!=cnt_fresh:
		        return -1
		    return t
		    
		n=len(grid)
		m=len(grid[0])
		q=deque()
		cnt_fresh=0
		t=0
		if n==0 or grid is None:
		    return 0
		for i in range(n):
		    for j in range(m):
		        if grid[i][j]==2:
		            q.append(((i,j),t))
		        if grid[i][j]==1:
		            cnt_fresh+=1

		if cnt_fresh==0:
		    return 0
		return bfs(grid,q,cnt_fresh)
		 


