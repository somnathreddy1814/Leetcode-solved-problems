class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        cnt=0
        for i in range(len(s)-2):
            st=set(s[i:i+3])
            if len(st)==3:
                cnt+=1
        return cnt
        
                
            
           
           
            
                
                

        
        
        
        
        
        
        
        
        
        
        
        
#         cnt=0
#         for i in range(len(s)-3+1):
#             temp=''
#             for j in range(i,i+3):
#                 if s[j] in temp:
#                     break
#                 else:
#                     temp+=s[j]
#                     if len(temp)==3:
#                         cnt+=1
                       
                
#         return cnt
            
            