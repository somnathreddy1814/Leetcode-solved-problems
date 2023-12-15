class Solution:
    def reverseWords(self, s: str) -> str:
        
        s=s.split()
        
        s=s[::-1]
        ans=" ".join(s)
        return ans
        
        