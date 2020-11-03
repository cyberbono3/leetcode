class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        
        
        
        
        mark desitnation as 1
        maze[destination[0]][destination[1]]  = 1
        maze[start[0]][start[1]]  = 1
        
            
        
        TC O(m*n)
        SC O(m*n)
        
            
            
        """
        def within_boundaries(x,y):
            return 0 <= x < R and 0 <= y < C
        
    
        def dfs(x,y):
            if (x,y) in visited:
                return False
            if [x,y] == destination:
                return True
            visited.add((x,y))
            for dx,dy in directions:
                nx, ny = x, y
                while within_boundaries(nx+dx,ny+dy) and not maze[nx+dx][ny+dy]:
                    nx += dx
                    ny += dy
                if dfs(nx,ny): 
                    return True
            return False
       
    
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        R, C = len(maze), len(maze[0])
        visited = set()
        return dfs(*start)
    
"""

class Solution(object):
    def hasPath(self, maze, start, destination):
        """
        :type maze: List[List[int]]
        :type start: List[int]
        :type destination: List[int]
        :rtype: bool
        
        
        
        
        mark desitnation as 1
        maze[destination[0]][destination[1]]  = 1
        maze[start[0]][start[1]]  = 1
        
            
        
        TC O(m*n)
        SC O(m*n)
        
            
            
        """
        def within_boundaries(x,y):
            return 0 <= x < R and 0 <= y < C
        
    
        directions = [(1,0), (0,1), (-1,0), (0,-1)]
        R, C = len(maze), len(maze[0])
        visited = set()
        stack = [(start[0], start[1])]
        while stack:
            x,y = stack.pop()
            if [x,y] == destination:
                return True
            visited.add((x,y))
            for dx,dy in directions:
                nx, ny = x, y
                while within_boundaries(nx+dx,ny+dy) and not maze[nx+dx][ny+dy]:
                    nx += dx
                    ny += dy
                if (nx,ny) in visited:
                    continue
                stack.append((nx,ny))
        return False
       





"""