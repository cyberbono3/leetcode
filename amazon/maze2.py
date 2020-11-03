
from heapq import heapify, heappush, heappop


class Solution:
    def shortestDistance(self, maze, start, destination):
      
        
        m, n = len(maze), len(maze[0])
        h = []
        heappush(h, (0, start[0], start[1]))
        dist = {}
        dist[(start[0], start[1])] = 0
        
        res = []
        while h:
            d, x, y = heappop(h)
            if [x, y] == destination:
                return d
            for dx,dy,dir in ((-1, 0, "l"), (1, 0, "r"), (0, -1, "u"), (0, 1, "d")):
                nx,ny,nd, ndir = x,y,d,dir
                while 0 <= nx + dx < m and 0 <= ny+dy  < n and maze[nx+dx][ny+dy] != 1:
                    nx += dx
                    ny += dy
                    nd += 1
                if (nx,ny) not in dist or nd < dist[(nx, ny)]:
                    dist[(nx, ny)] = nd
                    heappush(h, (nd, nx, ny))
        return -1