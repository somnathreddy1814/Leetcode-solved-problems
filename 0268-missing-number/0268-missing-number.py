class Solution:
    def missingNumber(self, nums1: List[int]) -> int:    
        sm=0
        for i in range(len(nums1)):
            sm+=i
        if max(nums1)==len(nums1)-1:
            return max(nums1)+1
        else:
            return sm-(sum(nums1)-max(nums1))
        
        
        
        
            
        
        