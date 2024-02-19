class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        result = []
        count = 0

        def level(count , root):
            if root == None :
                return 

            if len(result) <= count:
                result.append([])    
            
            result[count].append(root.val)
            count += 1
            level(count , root.left)
            level(count , root.right) 

        level(count , root)
        return result