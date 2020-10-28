
import copy


from collections import deque

class Solution(object):
    def slidingPuzzle(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        
        solved
        solved_state = [[1,2,3],[4,5,0]]
        
        
         board = [[1,2,3],
                  [4,0,5]]
                  
                 
         we fidn a coordinate of zero just traversing through mrows and cols O(R*C)
         we use bfs to count moves  O(V+E)
         TC O(R*C + (V+E))
         
         
         def swap()
         
         
         def bfs(r,c):
            q =[coordinate, mvoes]
            
            while q:
                corodinate moves
                corodinate, moves, board = q.popleft()
                if board == sovled_state:
                we return nmber of moves
                we identify neighbours by exploring 4 directions
                   we check if neighbor within boundaries
                    we hae new-board weith swapped elements
                      we swap and increment the nubmer of mvoes
            return -1
                      
         
         

        """
        def neighbours(r,c):
            # we explore nighbours in for directinns and check for boundaries
            for nr,nc in ((r,c+1), (r,c-1),(r+1,c),(r-1,c)):
                if 0 <= nr < R and 0 <= nc < C:
                    yield (nr,nc)
                    
        def swap(b,nr,nc,r,c):
            new_board = copy.deepcopy(b)
            new_board[nr][nc],new_board[r][c] = new_board[r][c], new_board[nr][nc]
            return new_board
                
        
        
        
        def bfs(r,c, board):
            q = deque()
            q.append((r,c,0,board))
            visited = set()
            while q:
                r,c,moves,b = q.popleft()
                visited.add(str(b))
                if b == solved_state:
                    return moves
                for (nr,nc) in neighbours(r,c):
                    new_board = swap(b,r,c,nr,nc)
                    if str(new_board) not in visited:
                        q.append((nr,nc,moves+1,new_board))
            return -1
                    
                
                

        solved_state = [[1,2,3],[4,5,0]]
        R, C = len(board), len(board[0])
        start = [(r,c) for c in range(C) for r in range(R) if not board[r][c]]
        empty = start.pop()
        return bfs(empty[0], empty[1], board)