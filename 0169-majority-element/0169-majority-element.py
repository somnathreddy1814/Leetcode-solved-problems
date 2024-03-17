class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        cnt=0
        ele=None
        for i in range(len(nums)):
            if cnt==0:
                ele=nums[i]
                cnt=1
            elif ele==nums[i]:
                cnt+=1
            else:
                cnt-=1
        c=0
        for i in range(len(nums)):
            if nums[i]==ele:
                c+=1
        if (c>=(len(nums)//2)):
            return ele
        return -1
                
        