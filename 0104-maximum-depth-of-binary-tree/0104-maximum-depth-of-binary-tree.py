# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #level order traversal then find length of levels
        if root is None:
            return 0
        res=[]
        q=deque()
        q.append(root)
        while(q):
            levels=[]
            for i in range(len(q)):
                temp=q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                levels.append(temp)
            res.append(levels)
        return len(res)
        