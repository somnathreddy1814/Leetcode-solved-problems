class Solution:
    def reverseWords(self, s: str) -> str:
        # lst=s.split()
        # for i,word in enumerate(lst):
        #     lst[i]=word[::-1]
        # print(lst)
        return " ".join([word[::-1] for word in s.split()])
            
        
        
            
        