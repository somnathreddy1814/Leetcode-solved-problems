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
            ls,lc=fun(node.left)
            rs,rc=fun(node.right)
            current_sum=node.val+ls+rs
            current_count=1+rc+lc
            if current_sum//current_count==node.val:
                res+=1
            return current_sum,current_count
        fun(root)
        return res
        