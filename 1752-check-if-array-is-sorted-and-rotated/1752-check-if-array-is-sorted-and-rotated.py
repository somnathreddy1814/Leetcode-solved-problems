class Solution:
    def check(self, nums: List[int]) -> bool:
        cnt=0
        for i in range(len(nums)-1):
            if nums[i]>nums[i+1]:
                cnt+=1
        return cnt==0 or cnt==1 and nums[-1]<=nums[0]
        