# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ans = []
        if root is None:
            return ans        
        q = deque()
        q.append(root)        
        while q:
            level_vals = []  # Store the values at the current level
            level_size = len(q)
            for _ in range(level_size):
                temp = q.popleft()
                level_vals.append(temp.val)
                
                if temp.left:
                    q.append(temp.left)
                if temp.right:
                    q.append(temp.right)
            
            ans.append(level_vals)  # Add the values at the current level to the result list
        
        return ans