
from  collections import deque


# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def distanceK(self, root, target, K):
        """
        :type root: TreeNode
        :type target: TreeNode
        :type K: int
        :rtype: List[int]
        
        edge cases:
        if not K:
            return [target]
        if not K not root.left and root.right:
            if root.val == target.val:
            return [root.val]
            
        
        
        
        Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2

        Output: [7,4,1]
        
        
        
        crate parent hashmap for every node
        run dfs for that
        
        
        run bfs to travrse through left child, right child and parent and then icnrease thedistance
        as soon as our distance reaches k weadd thevaleu to the result arrat
        
        
        5: [6,2,3]    
        3 : [5,1]
        

        """
        def dfs(node, par = None):
            if node:
                parent[node] = par
                dfs(node.left, node)
                dfs(node.right, node)
            
        parent = {}
        dfs(root)
        
        
        q = deque([(target, 0)])
        res = []
        seen = set()
        while q:
            node, dis = q.popleft()
            seen.add(node)
            if dis == K:
                res.append(node.val)
            for nei in (node.left, node.right, parent[node]):
                if nei and nei not in seen:
                    q.append((nei, dis+1))
        return res