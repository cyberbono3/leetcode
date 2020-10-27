from collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def widthOfBinaryTree(self, root):
        """
        :type root: TreeNode
        :rtype: int
        
        bfs
        
        set curr_depth to identify the first left most ndoe at the next level
        
        we output curr, pos depth 
        if the node is valid
           we append the children to the queue we do not check if parent is valid
           we identity the left most node by comparing depth with curr_depth
              if they do not match we set start pointter to pos
        we compute max width by pos - start + 1
        
        
        
        """
     
        
    
        q = deque()
        curr_depth = 0
        max_width = 0
        q.append((root, 0, 0 ))
        while q:
            curr, pos, d = q.popleft()
            if curr:
                q.append((curr.left,2**pos, d+1))
                q.append((curr.right,2**pos+1, d+1))
                # if we go to the next level 
                if curr_depth != d:
                    start = pos  # the leftmost node position
                    curr_depth = d
                # pso is current post
                max_width = max(max_width, pos - start +1 )
        return max_width
                                           
                               
                    