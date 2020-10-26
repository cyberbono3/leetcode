
from colelctions import deque

class Solution(object):
    def orangesRotting(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        if not grid:
            return 0
        
        # define the length of rows and columns
        C, R = len(grid[0]), len(grid)
        
        
       
        #add to the queue all rotting cells 
        q = deque()
        ones = []
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:
                    ones.append((r,c))
                elif grid[r][c] == 2:
                    q.append((r, c))
                    # 0 is number of minites
        if not ones:
            return 0
        
        #  find the neigbours
        def neighbors(r,c):
            for nr, nc in ((r, c+1), (r+1, c), (r-1, c), (r, c-1)):
                if  0 <= nr < R  and  0 <= nc < C and grid[nr][nc] == 1:
                    yield nr, nc
    
        # while loop pop the item the queue and make all neighbors equal 2
        l = 0 #level
        while q:
            size = len(q)
            for _ in range(size):
                row, col = q.popleft()
                for (nr,nc) in neighbors(row, col):
                    grid[nr][nc] = 2
                    q.append((nr,nc))
            l += 1
                    
                
        return -1 if any(grid[r][c] == 1 for (r,c) in ones) else l-1