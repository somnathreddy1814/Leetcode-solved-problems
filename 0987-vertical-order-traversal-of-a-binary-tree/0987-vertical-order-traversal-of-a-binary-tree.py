# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        queue = []  # store a layer of nodes a time
        queue.append((root,0,0))    # root, x, y
        dic = collections.defaultdict(list)
        # {"y":[all the nodes with the same y]}
        # node: (x,node.val) -> need to sort by x, and then val
        
        while queue: # deque way. insert to end, pop from the beginning. FIFO
            (node,x,y) = queue.pop(0)
            dic[y].append((x,node.val))
            if node.left:
                queue.append((node.left,x+1,y-1))
            if node.right:
                queue.append((node.right,x+1,y+1))

        return [[value for (x,value) in sorted(li)] for (y,li) in sorted(dic.items())] 
        