class Solution:
    def nextGreatestLetter(self, arr: List[str], target: str) -> str:
        if target>=arr[len(arr)-1]:
            return arr[0]
        low=0
        high=len(arr)-1
        res=-1
        while(low<=high):
            mid=(low+high)//2
            # if arr[mid]==target:
            #     return arr[mid]
            if arr[mid]>target:
                res=arr[mid]
                high=mid-1
            else:
                low=mid+1
        return res
        