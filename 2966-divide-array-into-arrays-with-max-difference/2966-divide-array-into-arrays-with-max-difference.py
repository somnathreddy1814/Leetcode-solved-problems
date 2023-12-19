class Solution:
    def divideArray(self, nums, k):
        nums.sort()
        
    
        ans=[]
        for i in range(2,len(nums),3):
            temp=[]
            if nums[i]-nums[i-2]<=k:
                temp.append(nums[i-2])
                temp.append(nums[i-1])
                temp.append(nums[i])
                ans.append(temp)
            else:
                return []
        return ans
            