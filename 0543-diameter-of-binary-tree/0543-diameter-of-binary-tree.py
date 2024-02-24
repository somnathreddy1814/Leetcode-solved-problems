# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans=0
        def diameter(node):
            nonlocal ans
            if node is None:
                return 0
            left=diameter(node.left)
            right=diameter(node.right)
            ans=max(ans,left+right)
            return 1+max(left,right)
        diameter(root)
        return ans
            
            
        