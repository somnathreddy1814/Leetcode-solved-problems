import sys
class Solution:
    def findMissingAndRepeatedValues(self, grid):
        length=len(grid)**2
        dct=defaultdict(int)
        
        sum1=0
        for i in range(len(grid)):
            for j in range(len(grid)):
                sum1+=grid[i][j]
                if grid[i][j] in dct:
                    dct[grid[i][j]]+=1
                else:
                    dct[grid[i][j]]=1
        a=0
        b=0
        sum2=0
        for i in range(1,length+1):
            sum2+=i
            if dct[i]==2:
                a=i
        
        b=sum2-sum1+a
        
        return [a,b]
                
