class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dct={}
        
        for i in range(len(nums)):
            if target-nums[i] in dct:
                return [dct[target-nums[i]],i]
            dct[nums[i]]=i
# class Solution:
#     def twoSum(self, arr: List[int], target: int) -> List[int]:
#         n=len(arr)
#         res={}
#         for i,num in enumerate(arr):
#             complement=target-num
#             if complement in res:
#                return [res[complement],i]
#             res[num]=i
    