class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(arr)
        ind=-1
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                ind=i
                break
        if ind==-1:
            return arr.reverse()
        for i in range(n-1,ind-1):
            if arr[i]>arr[ind]:
                arr[i],arr[ind]=arr[ind],arr[i]
                break
        arr[i+1:]=reversed(arr[i+1:])
        
class Solution:
    def nextPermutation(self, arr: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(arr)
        ind=-1
        for i in range(n-2,-1,-1):
            if arr[i]<arr[i+1]:
                ind=i
                break
        if ind==-1:
            return arr.reverse()

        for i in range(n-1,ind,-1):
            if arr[ind]<arr[i]:
                arr[ind],arr[i]=arr[i],arr[ind]
                break
        arr[ind+1:]=reversed(arr[ind+1:])


        