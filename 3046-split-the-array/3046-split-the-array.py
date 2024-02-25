class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        dct=collections.Counter(nums)
        for key,val in enumerate(dct):
            if dct[val]>2 or len(nums)%2!=0:
                return False
                break
                
        return True
        
        