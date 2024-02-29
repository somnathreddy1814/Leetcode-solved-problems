# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
#     def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
#         res=[]
#         q=deque()
#         q.append(root)
#         while(q):
#             levels=[]
#             for i in range(len(q)):
#                 temp=q.popleft()
#                 if temp.left:
#                     q.append(temp.left)
#                 if temp.right:
#                     q.append(temp.right)
#                 levels.append(temp.val)
#             res.append(levels)
#         print(res)
#         for i in range(len(res)):
#             for j in range(len(res[i])-1):
#                 if i%2==0:
#                     if res[i][j]%2!=0:
#                         if res[i][j]<res[i][j+1]:
#                             continue
#                         else:
#                             return False
#                     else:
#                         return False
#                 elif i%2!=0:
#                     if res[i][j]%2==0:
#                         if res[i][j]>res[i][j+1]:
#                             continue
#                         else:
#                             return False
#                     else:
#                         return False
#         return True
                    
                    
                    
# import collections
# class Solution:
    def isEvenOddTree(self, root: TreeNode) -> bool:
        queue = collections.deque([root])
        is_even = True
        while queue:
            prev = None
            for _ in range(len(queue)):
                node = queue.popleft()
                if is_even:
                    if node.val % 2 == 0: return False
                    if prev and prev.val >= node.val: return False
                else:
                    if node.val % 2 == 1: return False
                    if prev and prev.val <= node.val: return False
                if node.left: queue.append(node.left)
                if node.right: queue.append(node.right)
                prev = node
            is_even = not is_even
        return True                       
        
        