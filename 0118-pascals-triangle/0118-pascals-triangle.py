class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        def genRow(n):
            ansRow=[1]
            ans=1
            for i in range(n):
                ans*=(n-i)
                ans//=(i+1)
                ansRow.append(ans)
            return ansRow
        n=numRows
        final=[[1]]
        for i in range(1,n):
            final.append(genRow(i))
        return final
            
       
            
            
            
            
        
        