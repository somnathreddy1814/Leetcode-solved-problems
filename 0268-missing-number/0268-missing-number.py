class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum1=0
        sum2=0
        
        
        for i in range(len(nums)):
            sum1+=nums[i]
        # print(sum1)
        for i in range(max(nums)+1):
            sum2+=i
        # print(sum2)
        if sum2-sum1==0 and min(nums)==0:
            return max(nums)+1
        elif sum2-sum1==0 and min(nums)!=0:
            return 0
        else:
            return sum2-sum1
            
        
        