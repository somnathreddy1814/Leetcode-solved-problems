class Solution:
    def maximumSubarraySum(self, arr: List[int], k: int) -> int:
        i=0
        j=0
        sm=0
        mxsm=0
        seen=defaultdict(int)
        while(j<len(arr)):
            if arr[j] not in seen:
                sm+=arr[j]
                seen[arr[j]]=1
                if j-i+1<k:
                    j+=1
                elif j-i+1==k:
                    mxsm=max(mxsm,sm)
                    sm-=arr[i]
                    del seen[arr[i]]
                    i+=1
                    j+=1
            else:
                sm-=arr[i]
                del seen[arr[i]]
                i+=1
        return mxsm
                
            
        