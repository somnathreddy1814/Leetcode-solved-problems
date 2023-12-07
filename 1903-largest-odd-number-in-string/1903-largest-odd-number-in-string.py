class Solution:
    def largestOddNumber(self, num: str) -> str:
        odd='13579'
        for i in range(len(num)-1,-1,-1):
            if num[i] in odd:
                return num[0:i+1]
        return ""
        
            
        