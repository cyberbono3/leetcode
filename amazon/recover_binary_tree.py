# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        
        inorder traversal
        
        compare which elements are swapped 
        
        then run dfs to swap these elements return root
        
        
        def inorder(node):
            if not node: return []
            return inorder(node.left) + [node.val] + inorder(node.right)
            
        inrdoer =       [1,3,2]
        sorted_inorder= [1,2,3]
        
        swapped = [a for (a,b) in zip(inorder, sorted_inorder) if a != b]
        swapped = [3,2]
        
        
        stack = [root]
        
        whel stack:
            curr = stack.pop()
            if curr.val == swapped[0]:
                curr.val = swapped[1]
            elif curr.val = seapped[1]:
                curr.val = swapped[0]
            if curr.left 
            
        return root
                