class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trusts_count=[0]*(n+1)#voter
        trusted_count=[0]*(n+1)#judge candidate
        for a,b in trust:
            trusts_count[a]+=1
            trusted_count[b]+=1
        for i in range(1,n+1):
            if trusts_count[i]==0 and trusted_count[i]==n-1:
                return i
        return -1
        