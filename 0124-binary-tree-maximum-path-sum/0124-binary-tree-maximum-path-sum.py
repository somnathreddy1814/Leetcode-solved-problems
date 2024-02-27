# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        mx=float("-inf")
        def fun(node):
            nonlocal mx
            if node is None:
                return 0
            left=max(fun(node.left),0)
            right=max(fun(node.right),0)
            path=node.val+left+right
            mx=max(mx,path)
            return node.val+max(left,right)
        fun(root)
        return mx