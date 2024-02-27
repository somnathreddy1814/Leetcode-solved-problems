# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, node: Optional[TreeNode]) -> List[List[int]]:
        ans=[]
        if node is None:
            return []
        q=deque()
        q.append(node)
        while(q):
            levels=[]
            for i in range(len(q)):
                temp=q.popleft()
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
                levels.append(temp.val)
            ans.append(levels)
        for i in range(len(ans)):
            if i%2!=0:
                ans[i]=ans[i][::-1]
        return ans
            
        
        