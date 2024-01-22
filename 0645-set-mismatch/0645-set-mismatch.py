class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        n,a,b=len(nums),sum(nums),sum(set(nums))
        s=sum([i for i in range(1,n+1)])
        return [a-b,s-b]