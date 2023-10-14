class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        s=list(s)
        n=len(s)
        i=0
        while i<n:
            start=i
            end=min(i+k,n)
            s[start:end]=reversed(s[start:end])
            i+=2*k
        return ''.join(s)
