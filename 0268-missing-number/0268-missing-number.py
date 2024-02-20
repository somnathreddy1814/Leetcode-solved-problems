class Solution:
    def missingNumber(self, nums1: List[int]) -> int:    
        nums2=[i for i in range(len(nums1))]
        if max(nums1)==max(nums2):
            return max(nums1)+1
        else:
            return sum(nums2)-(sum(nums1)-max(nums1))
        
        
        
        
            
        
        