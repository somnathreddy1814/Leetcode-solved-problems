class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sm=[]
        sum=0
        for i in range(len(nums)):
            sum+=nums[i]
            sm.append(sum)
        return sm
            
            