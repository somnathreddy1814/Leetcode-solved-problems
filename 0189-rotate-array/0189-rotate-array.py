class Solution:
    def rotate(self, arr: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(arr)
        k=k%n
        if n==0:
            return
        def reverse(arr,start,end):
            while(start<end):
                arr[start],arr[end]=arr[end],arr[start]
                start+=1
                end-=1
        reverse(arr,0,n-1)
        reverse(arr,0,k-1)
        reverse(arr,k,n-1)
        
        