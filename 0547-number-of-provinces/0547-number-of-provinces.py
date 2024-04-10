class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n=len(isConnected)
        m=len(isConnected[0])
        adj=[[]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if isConnected[i][j]==1 and i!=j:
                    adj[i].append(j)
                    adj[j].append(i)
                    
                    
        def dfs(node,adj,vis):
            vis[node]=1
            for i in adj[node]:
                if not vis[i]:
                    dfs(i,adj,vis)
        vis=[0]*n
        cnt=0
        for i in range(n):
            if vis[i]==0:
                cnt+=1
                dfs(i,adj,vis)
        return cnt
