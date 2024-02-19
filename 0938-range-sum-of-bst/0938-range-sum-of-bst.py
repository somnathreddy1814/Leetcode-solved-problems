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
                elif node.val<low:
                    sem(node.right)
                else:
                    sem(node.left)
        sem(root)
        return sm
            
            
                
class Solution:
    def rangeSumBST(self, root: TreeNode, low: int, high: int) -> int:
        def dfs(node):
            if not node:
                return
            if low <= node.val <= high:
                self.total_sum += node.val
                dfs(node.left)
                dfs(node.right)
            elif node.val < low:
                dfs(node.right)
            elif node.val > high:
                dfs(node.left)

        self.total_sum = 0
        dfs(root)
        return self.total_sum