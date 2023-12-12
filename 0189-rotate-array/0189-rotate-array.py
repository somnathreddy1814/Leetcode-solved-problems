class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        if k> len(nums):
            k=k%len(nums)
            
        my_dic={}
        my_dic['first']=(nums[-k:])
        my_dic['second']=nums[:-k]
        nums[:]=my_dic['first'] + my_dic['second']
        