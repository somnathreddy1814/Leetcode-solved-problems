# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        final_sum=0
        if root is None:
            return final_sum
        def temp_sum(node):
            nonlocal final_sum
            if node:
                if low<=node.val<=high:
                    final_sum+=node.val
                    temp_sum(node.left)
                    temp_sum(node.right)
                elif low>node.val:
                    temp_sum(node.right)
                else:
                    temp_sum(node.left)
        temp_sum(root)
        return final_sum
        