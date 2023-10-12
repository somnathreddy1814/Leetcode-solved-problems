class Solution:
    def reverseWords(self, s: str) -> str:
        def rev(start,end):
            return s[start:end][::-1]
        res=""
        start=0
        for end in range(len(s)):
            if s[end]==" ":
                res+=rev(start,end)+" "
                start=end+1
            elif(end==len(s)-1):
                res+=rev(start,end+1)
        return res
                
                
                
        
            
        
        
            
        