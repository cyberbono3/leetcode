"""

305. Number of Islands II
Hard

921

22

Add to List

Share
A 2d grid map of m rows and n columns is initially filled with water. We may perform an addLand operation which turns the water at position (row, col) into a land. Given a list of positions to operate, count the number of islands after each addLand operation. An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example:

Input: m = 3, n = 3, positions = [[0,0], [0,1], [1,2], [2,1]]
Output: [1,1,2,3]
Explanation:

Initially, the 2d grid grid is filled with water. (Assume 0 represents water and 1 represents land).

0 0 0
0 0 0
0 0 0
Operation #1: addLand(0, 0) turns the water at grid[0][0] into a land.

1 0 0
0 0 0   Number of islands = 1
0 0 0
Operation #2: addLand(0, 1) turns the water at grid[0][1] into a land.

1 1 0
0 0 0   Number of islands = 1
0 0 0
Operation #3: addLand(1, 2) turns the water at grid[1][2] into a land.

1 1 0
0 0 1   Number of islands = 2
0 0 0
Operation #4: addLand(2, 1) turns the water at grid[2][1] into a land.

1 1 0
0 0 1   Number of islands = 3
0 1 0
Follow up:

Can you do it in time complexity O(k log mn), where k is the length of the positions?






"""

class Solution(object):
    def numIslands2(self, m, n, positions):
        """
        :type m: int
        :type n: int
        :type positions: List[List[int]]
        :rtype: List[int]
        
        input constraints
         0 <= n < 100
         0 <= m < 100
         0 <= positions  < 100
         inputs only 0,1
         
        edge cases:
            m, n , positions
            
         
        output list of islands
        
        
        1 0 0     [0,0]      result = [1]
        0 0 0
        0 0 0
        
        
        1 1 0     [0,1]      result = [1]
        0 0 0     from (0,1) we have to check neighbours if neighbour equls one , then we dont icnrement number of islands
        0 0 0
        
        1 1 0      [1,2,]
        0 0 1       from (1,2) we check neighbours if there are no neighbours equal 1 we icnrement number of 
        0 0 0
        
        1 1 0
        0 1 1     
        0 0 1
        
        
        1 1 0
        0 0 1     
        0 1 1
        
        
        def neighbours(x,y):
            we check horizonal vertical and we check boundaries if neighbour equals 1 we return it
            
            
        
        
        board = [[0]*n for _ in range(m)]
        R, C = len(board), len(board[0])
        
        loop over positions  
            neis = neighbours(pos_x,pos_y)
            if not neis:
               we increment num of islands
            else:
                case 1
                if nei only one:
                    we do nothing 
                case 2
                   if neis are two 
                   we decrement
                
            board[pos_x][pos_y]  = 1
        
        """
        def neighbours(r,c):
            # exlore enighbours
            nei_count = 0
            for (nr,nc) in ((r+1, c), (r-1,c), (r,c+1,), (r,c-1)):
                if  0 <= nr < R and 0 <= nc < C and board[nr][nc]:
                    nei_count += 1
            return nei_count
                    
            
        
        count = 0
        board = [[0]*n for _ in range(m)]
        R, C = m, n
        
        res = []
        for x,y in positions:
            board[x][y] = 1
            nei_count = neighbours(x,y)
            if not nei_count:
                count += 1
            else:
                if count > 1:
                    if nei_count == count:
                        count -= 1 
            res.append(count)
        return res
        
            
            
        
        
        
        