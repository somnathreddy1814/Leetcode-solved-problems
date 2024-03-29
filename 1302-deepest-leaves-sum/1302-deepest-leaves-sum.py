# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:
        q=deque()
        q.append(root)
        res=[]
        while(q):
            levels=[]
            for i in range(len(q)):
                temp=q.popleft()
                if temp.left is not None:
                    q.append(temp.left)
                if temp.right is not None:
                    q.append(temp.right)
                levels.append(temp.val)
            res.append(levels)
        return sum(res[-1])
        