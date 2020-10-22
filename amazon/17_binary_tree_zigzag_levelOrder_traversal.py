from collections import deque 


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return None
        
        q = deque()
    
    
        q.append(root)
        level_number = 0
        res = []
        
        while q:
            size = len(q)
            level = []
            
            for _ in range(size):
                curr = q.popleft()
                level.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            
            if not level_number % 2:
                # level number is even
                res.append(level)
            else:
                #level nubme is odd
                res.append(level[::-1])
            level_number += 1
        return res
                
                
                             