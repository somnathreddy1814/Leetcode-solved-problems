class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dct=Counter(nums)
        # print(dct)
        ans=[]
        for key,val in dct.items():
            if dct[key]>1:
                ans.append(key)
        return ans