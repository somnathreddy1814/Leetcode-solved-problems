class Solution:
    def reverseWords(self, s: str) -> str:
        lst=s.split()
        for i,word in enumerate(lst):
            lst[i]=word[::-1]
        print(lst)
        return " ".join(lst)
            
        
        
            
        