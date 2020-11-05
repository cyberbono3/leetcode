# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    s = 0
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        
        
        
                10
               /  \
              5   15
             / \    \
            3  7    18
            
            
            if curr.val > R:
                 add the left node it is highly possible left node witill be in range
            if curr.rval  < L:
                stack.append(curr.right
            
            l = 5 , R = 15 includisive)
            
            top down 
            
            stack = [root]
            total = 0
            whiel stack:
                curr = stack.pop()
                if  L <= curr.val <= R:
                    total += curr.val
                if curr.left:
                    stack.append(curr.left)
                
                    
                
                    
      
        
        """
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    Solution.s += node.val
                    dfs(node.left)
                    dfs(node.right)
                elif node.val < L:
                    dfs(node.right)
                elif node.val > R:
                    dfs(node.left)
        dfs(root)
        return Solution.s