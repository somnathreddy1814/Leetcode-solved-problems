class Solution:
    def findMinimumOperations(self, s1: str, s2: str, s3: str) -> int:
        mn_ln=min(len(s1),len(s2),len(s3))
        sm_ln=len(s1)+len(s2)+len(s3)
        max_sum=sm_ln
        if s1[0]!=s2[0] or s2[0]!=s3[0] or s3[0]!=s1[0]:
            return -1
        
        else:
            for i in range(mn_ln):
                if s1[i]==s2[i]==s3[i]:
                    max_sum-=3
                else:
                    break
            return max_sum
                    
            
        