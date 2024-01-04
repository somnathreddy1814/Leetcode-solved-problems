class Solution:
    def minOperations(self, nums: List[int]) -> int:
        dct=Counter(nums)
        count=list(dct.values())
        ans=0
        for num in count:
            if num==1:
                return -1
            ans+=num//3
            if num%3:
                ans+=1
        
        return ans
