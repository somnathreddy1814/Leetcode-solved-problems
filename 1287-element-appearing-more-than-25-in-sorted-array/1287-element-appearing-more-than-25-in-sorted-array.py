class Solution(object):
    def findSpecialInteger(self, arr):
        cnts=defaultdict(int)
        for num in arr:
            cnts[num]+=1
        target=len(arr)//4
        for key,value in cnts.items():
            if value>target:
                return key
        return -1
        