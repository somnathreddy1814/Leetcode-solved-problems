class Solution:
    def minimumLength(self, s: str) -> int:
        i=0
        j=len(s)-1
        while i<j and s[i]==s[j]:
            ch=s[i]
            while i<=j and ch==s[i]:
                i+=1
            while i<=j and ch==s[j]:
                j-=1
        return j-i+1
    
       