class Solution:
    def findCircleNum(self, A):
        adj=[[] for i in range(len(A))]
        for i in range(len(A)):
            for j in range(len(A)):
                if(A[i][j]==1 and i!=j):
                    adj[i].append(j)
                    adj[j].append(i)
                    
        
        def dfs(node,vis):
            vis[node]=1
            for i in adj[node]:
                if vis[i]==0:
                    dfs(i,vis)
        
        v=len(adj)
        vis=[0]*(v+1)
        cnt=0
        for i in range(v):
            if vis[i]==0:
                cnt+=1
                dfs(i,vis)
        return cnt