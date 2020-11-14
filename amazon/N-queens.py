class Solution(object):
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        
        def safe_place(r, c, choices):
            
            find_safe = True
            
            for row, col in choices:
                if row + col == r + c or row - col == r - c or col == c:
                    find_safe = False
                    break
            
            return find_safe
                    
    
        def solve_puzzle(row, choices):
            if row == R:
                return True
            else:
                for col in range(C):
                    if safe_place(row, col, choices):
                        choices.append((row, col))
                        if solve_puzzle(row+1, choices):
                            return True
                        choices.pop()
                return False
            
        def print_result():
            result = [None]*len(res)
            for i, solution in enumerate(res):
                chess_board = [None]*R
                for r in range(R):
                    s = ""
                    for c in range(C):
                        if c == solution[r][1]:
                            s += "Q"
                        else:
                            s += "."
                    chess_board[r] = "".join(s)
                result[i] = chess_board
            return result
    
           
                
                            
        R, C = n, n
        res = []
        for c in range(C):
            choices = []
            choices.append((0, c))
            if solve_puzzle(1, choices):
                res.append(choices)
        return print_result()