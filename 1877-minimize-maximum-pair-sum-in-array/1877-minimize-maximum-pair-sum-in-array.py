class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        i=0
        j=len(nums)-1
        mx=0
        sm=0
        while(i<j):
            sm+=nums[i]+nums[j]
            mx=max(mx,sm)
            sm=0
            i+=1
            j-=1
        return mx
            
            
            
            