
class Solution(object):
    def numDistinctIslands(self, grid):
        
        def neighbours(r,c):
            for nr,nc in ((r+1,c), (r-1,c), (r, c+1), (r,c-1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc]:
                    yield nr,nc
        
        
        def dfs(r,c,r0,c0):
            stack = [(r,c,r0,c0)]
            shape = set()
            while stack:
                r,c,r0,c0 = stack.pop()
                grid[r][c] = 0
                shape.add((r-r0,c-c0))
                for (nr,nc) in neighbours(r,c):
                    stack.append((nr,nc,r0,c0))
            return shape
                    
        
        
        shapes = set()
        R, C = len(grid),len(grid[0])
        for r in range(R):
            for c in range(C):
                if grid[r][c]:
                    shape = dfs(r,c,r,c)
                    shapes.add(tuple(shape))
        return len(shapes)
                
