class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        adj=[[] for _ in range(len(isConnected))]
        for i in range(len(isConnected)):
            for j in range(len(isConnected)):
                if (isConnected[i][j]==1 and i!=j):
                    adj[i].append(j)
                    adj[j].append(i)
        def dfs(node,adj,vis):
            vis[node]=1
            for i in adj[node]:
                if vis[i]==0:
                    dfs(i,adj,vis)
                    
        v=len(adj)
        vis=[0]*(v+1)
        cnt=0
        for i in range(v):
            if vis[i]==0:
                cnt+=1
                dfs(i,adj,vis)
        return cnt
        