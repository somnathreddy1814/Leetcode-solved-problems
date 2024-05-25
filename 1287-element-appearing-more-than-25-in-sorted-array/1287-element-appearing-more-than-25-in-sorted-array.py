class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        dct=Counter(arr)
        
        for key,val in dct.items():
            if val>len(arr)//4:
                return key