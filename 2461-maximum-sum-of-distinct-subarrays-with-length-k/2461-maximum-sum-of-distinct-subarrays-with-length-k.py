class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        sm=0
        mxsm=0
        i=0
        j=0
        seen=defaultdict(int) #using dictonary as removing an element T.C is O(1)
        while(j<len(nums)):
            if nums[j] not in seen:
                sm+=nums[j]
                seen[nums[j]]=1
                if j-i+1<k:
                    j+=1
                elif j-i+1==k:
                    mxsm=max(mxsm,sm)
                    # print(mxsm)
                    sm-=nums[i]
                    del seen[nums[i]]
                    i+=1
                    j+=1
                    
            else:
                sm-=nums[i]
                del seen[nums[i]]
                i+=1
                    
                
        return mxsm
