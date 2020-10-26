
from collections import deque

class Solution(object):
    def cutOffTree(self, forest):
        """
        :type forest: List[List[int]]
        :rtype: int
        
        
        # edge cases
        for len(forest)  =1
        
        
        
        bfs
        q = [(0, 0, 0)]
        
        while q:
            r,c,steps from the queu
            we discover all the neighbours that hava height > 1:
                we check if this neighbours within bouard bondaries
                    we sort the noigbours by the height 
                    
                        we cut the tree and make the node is visied
                          node = 1
                
                
        if board contains only ones and zeroes it means  we cut all the trees
         
        
        """
        def neighbours(r, c, visited):
            res = []
            for (nr,nc) in ((r+1, c), (r-1,c), (r, c+1), (r,c-1)):
                if 0 <= nr < R and  0 <= nc < C and (nr,nc) not in visited and forest[nr][nc] > 1:
                    res.append((nr,nc))
            return res
            
            
            
        def find_valid_cells():
            valid_cells = []
            for r in range(R):
                for c in range(C):
                    if forest[r][c] >= 1:
                        valid_cells.append((r,c))
            return valid_cells
                        
                        
        R, C = len(forest), len(forest[0])
        
        visited = set()
        #steps = 0
        
        q = deque()
        q.append((0,0,0))
    
        while q:
            r,c,steps = q.popleft()
            visited.add((r, c))
            neis = neighbours(r,c, visited)
            for nei in sorted(neis):
                nr,nc = nei[0], nei[1]
                forest[nr][nc] = 1
                q.append((nr,nc, steps+1))
     
        cells = find_valid_cells()
        return steps if all(forest[r][c] == 1 for r,c in cells) else -1
        
                    
                    
        