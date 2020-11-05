class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        
        
        loop over rows and cols
          if you hit
          x just explore neighbours if they are battleships
          made them dots ( visited)
          increment counter 
    
        
        """
        
        count = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == ".":
                    continue
                elif i > 0 and board[i-1][j] == "X":
                    continue
                elif j > 0 and board[i][j-1]  == "X":
                    continue
                else:
                    count += 1
        return count
                