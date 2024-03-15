class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        tot=0
        for i in range(1,max(nums)+1):
            tot+=i
        actual=0
        for i in range(len(nums)):
            actual+=nums[i]
        
        if tot-actual==0:
            if 0 in nums:
                return max(nums)+1
            else:
                return 0
        else:
            return tot-actual
            
            
        