# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        ans=[]
        if root is None:
            return sum(ans)
        def sm(node):
            if node:
                if low<=node.val<=high:
                    ans.append(node.val)
                sm(node.left)
                sm(node.right)
        sm(root)
        return sum(ans)
            
            
                
