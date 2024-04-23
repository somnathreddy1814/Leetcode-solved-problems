from collections import defaultdict
class Solution:
    def subarraySum(self, arr: List[int], k: int) -> int:
        mpp=defaultdict(int)
        presum=0
        cnt=0
        n=len(arr)
        mpp[0]=1
        for i in range(n):
            presum+=arr[i]
            remove=presum-k
            cnt+=mpp[remove]
            mpp[presum]+=1
        return cnt
        
        