class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        k=k%len(arr)
        def rev(arr,start,end):
            while(start<end):
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        
        rev(arr,0,len(arr)-1)
        rev(arr,0,k-1)
        rev(arr,k,len(arr)-1)
        
        