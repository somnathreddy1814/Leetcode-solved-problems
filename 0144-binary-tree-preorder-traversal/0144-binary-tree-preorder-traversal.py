# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans=[]
        if root is None:
            return ans
        stack=[root]
        while(stack):
            top_node=stack.pop()
            ans.append(top_node.val)
            if top_node.right is not None:
                stack.append(top_node.right)
            if top_node.left is not None:
                stack.append(top_node.left)
        return ans
            