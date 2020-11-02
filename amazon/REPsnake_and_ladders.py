
import collections


class Solution(object):
    def snakesAndLadders(self, board):
        """
        :type board: List[List[int]]
        :rtype: int
        """
        #translat label to coodordinates x,y
        def translate(label):
            pass
        
        n = len(board)
        q = collections.deque([(1, 0)])
        seen = set()
        while q: 
            size = len(q)
            for _  in range(size):
                label, moves = q.popleft()
                seen.add(label)
                if label == n*n:
                    return moves 
                r,c = translate(label)
                if board[r][c] != -1:
                    label = board[r][c]
                for x in range(1,7):
                    new_label = label + x
                    if new_label <= n*n and new_label not in seen:
                        q.append(new_label, moves+1)
        return -1
                        
                
         