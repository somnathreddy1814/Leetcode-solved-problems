# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfSubtree(self, root) -> int:
        res=0
        def fun(node):
            nonlocal res
            if node is None:
                return 0,0
            left_sum,left_count=fun(node.left)
            right_sum,right_count=fun(node.right)
            curr_sum=node.val+left_sum+right_sum
            curr_count=1+left_count+right_count
            if curr_sum//curr_count==node.val:
                res+=1
            
            return curr_sum,curr_count
        fun(root)
        return res
        