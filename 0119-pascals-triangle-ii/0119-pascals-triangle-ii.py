class Solution:
    def getRow(self, rowIndex: int) ->List[int]:
        if rowIndex==0:
            return [1]
        tmp=[0]+self.getRow(rowIndex-1)+[0]
        res=[]
        for i in range(len(tmp)-1):
            res.append(tmp[i]+tmp[i+1])
        return res