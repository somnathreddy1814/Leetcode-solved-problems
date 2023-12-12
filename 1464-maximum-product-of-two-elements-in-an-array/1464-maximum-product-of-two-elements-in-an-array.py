class Solution:
    def maxProduct(self, nums: List[int]) -> int:
#         mx=0
#         for i in range(len(nums)):
#             for j in range(i+1,len(nums)):
#                 mx=max(mx,(nums[i]-1)*(nums[j]-1))
                
#         return mx
        nums.sort()
        
        return (nums[-1]-1)*(nums[-2]-1)
                