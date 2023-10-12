class Solution:
    def first(self,arr,target):
        n=len(arr)
        low=0
        high=n-1
        first=-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]==target:
                first=mid
                high=mid-1
            elif arr[mid]>target:
                
                high=mid-1
            else:
                low=mid+1
                
        return first

    def last(self,arr,target):
        n=len(arr)
        low=0
        high=n-1
        last=-1
        while(low<=high):
            mid=(low+high)//2
            if arr[mid]==target:
                last=mid
                low=mid+1
            elif arr[mid]<target:
                low=mid+1
            else:
                high=mid-1
        return last

    def searchRange(self, arr: List[int], target: int) -> List[int]:
        fo=self.first(arr,target)
        if fo==-1:
            return [-1,-1]
        else:
            return [fo,self.last(arr,target)]
        