class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans=[]
        nums.sort()
        def subsethelper(ind,nums,temp):
            if ind==len(nums):
                ans.append(temp) if temp not in ans else None
                return
            subsethelper(ind+1,nums,temp+[nums[ind]])
            subsethelper(ind+1,nums,temp)
        subsethelper(0,nums,temp=[])
        return ans
