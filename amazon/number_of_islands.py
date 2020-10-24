"""

https://leetcode.com/problems/number-of-islands/

Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

 

Example 1:

Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1
Example 2:

Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3
 
 
Constraints:

m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
 

"""
#   O(R*C*n)
class Solution(object):
    def numIslands(self, grid):
        def neighbours(r,c):
            for nr,nc in ((r+1, c), (r-1, c), (r, c+1), (r, c-1)):
                if 0 <= nr < R and 0 <= nc < C and grid[nr][nc] == "1":
                    yield (nr,nc)
            
    
        def dfs(r,c):
            stack = [(r,c)]
            while stack:
                r, c = stack.pop()
                #mark as visited
                grid[r][c] = "0"
                for (nr,nc) in neighbours(r,c):
                    stack.append((nr,nc))
                    
        
        if not grid: return 0
        R, C = len(grid), len(grid[0])
        
        count = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    dfs(r,c)  
                    count += 1     
        return count
        
         
sol = Solution()
print(sol.numIslands([["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]])  == 1)
print(sol.numIslands([["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]])  == 3)
        