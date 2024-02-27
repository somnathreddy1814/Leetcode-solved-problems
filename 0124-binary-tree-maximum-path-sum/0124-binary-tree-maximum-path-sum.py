# # Definition for a binary tree node.
# # class TreeNode:
# #     def __init__(self, val=0, left=None, right=None):
# #         self.val = val
# #         self.left = left
# #         self.right = right
# class Solution:
#     def maxPathSum(self, root: Optional[TreeNode]) -> int:
#         mx=0
#         mx_path=0
#         def fun(node):
#             nonlocal mx
#             nonlocal mx_path
            
#             if node is None:
#                 return 0
#             left=max(fun(node.left),0)
#             right=max(fun(node.right),0)
#             mx=node.val+left+right
#             mx_path=max(mx,mx_path)
#             return node.val+max(left,right)
#         fun(root)
#         return mx_path
            
            
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.max_path = float("-inf")
        self.helper(root)
        
        return self.max_path
        
    def helper(self, root):
        if not root:
            return 0
        
        left_res = max(self.helper(root.left), 0)
        right_res = max(self.helper(root.right), 0)
        
        # can use both child for current root
        max_path_for_this_root = root.val + left_res + right_res
        self.max_path = max(self.max_path, max_path_for_this_root)
        
        # to be added to parent path, can only pick one of the child
        return root.val + max(left_res, right_res)  