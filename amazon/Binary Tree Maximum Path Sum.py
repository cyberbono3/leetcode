# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    maxPath = float("-inf")
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
           -2
             \
             -1
        
        
        
        
        """
        def dfs(node):
            if not node:
                return 0
            left, right = max(dfs(node.left), 0), max(dfs(node.right), 0)
            s = left + right + node.val
            self.maxPath = max(self.maxPath, s)
            return node.val + max(left, right)
        
        if not root.left and not root.right:
            return root.val
        dfs(root)
        return self.maxPath
            
        