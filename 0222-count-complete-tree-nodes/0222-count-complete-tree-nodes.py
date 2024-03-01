# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        res=0
        
        def preorder(node):
            nonlocal res
            if node is None:
                return 0
            res+=1
            preorder(node.left)
            preorder(node.right)
            return res
        preorder(root)
        return res