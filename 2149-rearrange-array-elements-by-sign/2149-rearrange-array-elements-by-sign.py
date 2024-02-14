class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives=[]
        negatives=[]
        for i in range(len(nums)):
            if nums[i]>0:
                positives.append(nums[i])
            else:
                negatives.append(nums[i])
        
        res=[]
        for i in range(len(nums)//2):
            res.append(positives[i])
            res.append(negatives[i])
            
        return res
            
        