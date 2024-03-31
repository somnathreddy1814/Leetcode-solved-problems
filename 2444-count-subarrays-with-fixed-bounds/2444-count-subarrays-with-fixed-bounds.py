class Solution:
    def countSubarrays(self, nums: List[int], minK: int, maxK: int) -> int:
        i=j=k=-1
        res=0
        for ind,val in enumerate(nums):
            if not minK<=val<=maxK:
                k=ind
            if val==minK:
                i=ind
            if val==maxK:
                j=ind
            res+=max(0,min(i,j)-k)
        return res
                
    