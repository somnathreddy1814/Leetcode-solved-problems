class Solution:
    def frequencySort(self, s: str) -> str:
        count=Counter(s)
       
        ans=[]
        for key,val in count.most_common():
            ans+=[key]*val
        return "".join(ans)
