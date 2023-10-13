class Solution:
    def maxSlidingWindow(self, arr: List[int], k: int) -> List[int]:
        i=0
        j=0
        res=[]
        dq=deque()
        while(j<len(arr)):
            while dq and dq[-1]<arr[j]:
                dq.pop()
            dq.append(arr[j])
            
            if j-i+1==k:
                res.append(dq[0])
                if dq[0]==arr[i]:
                    dq.popleft()
                i+=1
            j+=1
        
        return res
            
        
        