class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cnt1=0
        cnt2=0
        ele1=float('inf')
        ele2=float('inf')
        for i in range(len(nums)):
            if cnt1==0 and nums[i]!=ele2:
                cnt1=1
                ele1=nums[i]
            elif cnt2==0 and nums[i]!=ele1:
                cnt2=1
                ele2=nums[i]
            elif ele1==nums[i]:
                cnt1+=1
            elif ele2==nums[i]:
                cnt2+=1
            else:
                cnt1-=1
                cnt2-=1
        cnt1=0
        cnt2=0
        for i in range(len(nums)):
            if nums[i]==ele1:
                cnt1+=1
            elif nums[i]==ele2:
                cnt2+=1
        ans=[]
        mn=int(len(nums)/3)+1
        if cnt1>=mn:
            ans.append(ele1)
        if cnt2>=mn:
            ans.append(ele2)
        return ans
  