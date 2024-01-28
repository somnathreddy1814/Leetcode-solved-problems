class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        ans = []
        stack = [root]
        
        while stack:
            temp = stack.pop()
            
            if temp:
                ans.append(temp.val)
                stack.append(temp.right) #as we are using stack which works on LIFO, we need to push right tree first so that left will be popped out
                stack.append(temp.left)
                
        return ans