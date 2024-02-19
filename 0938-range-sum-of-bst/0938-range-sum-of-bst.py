# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        sm=0
        if root is None:
            return sm
        def sem(node):
            nonlocal sm
            if node:
                if low<=node.val<=high:
                    sm=sm+node.val
                sem(node.left)
                sem(node.right)
        sem(root)
        return sm
            
            
                
