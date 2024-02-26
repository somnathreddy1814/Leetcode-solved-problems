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
        def preorder(node,tree):
            if node is None:
                tree.append("null")
                return 0
            tree.append(node.val)
            preorder(node.left,tree)
            preorder(node.right,tree)
            
            
            return tree
        res1=preorder(p,res1)
        res2=preorder(q,res2)
        print(res1)
        print(res2)
        return res1==res2 
            
        