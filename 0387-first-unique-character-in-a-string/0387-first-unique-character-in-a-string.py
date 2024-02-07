class Solution:
    def firstUniqChar(self, s: str) -> int:
        count=Counter(s)
       
        ind=-1
        for i in range(len(s)):
            if count[s[i]]==1:
                ind=i
                break
            else:
                continue
        return ind
        
            
            
            
            
        
        