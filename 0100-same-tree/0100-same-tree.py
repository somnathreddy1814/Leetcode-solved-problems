# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        res1=[]
        res2=[]
        def inorder(node,tree):
            if node is None:
                tree.append("null")
                return 0
            tree.append(node.val)
            inorder(node.left,tree)
            inorder(node.right,tree)
            
            
            return tree
        res1=inorder(p,res1)
        res2=inorder(q,res2)
        print(res1)
        print(res2)
        return res1==res2 
            
        