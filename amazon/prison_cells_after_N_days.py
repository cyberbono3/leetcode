class Solution(object):
    def prisonAfterNDays(self, cells, N):
        """
        :type cells: List[int]
        :type N: int
        :rtype: List[int]
        
            300   0 0  0 0  0 0  00
            
            
            285   0  0 0 0  0 0  0 0
            
            
                                         7
            Day 0: [0, 1, 0, 1, 1, 0, 0, 1]
                    -1    +1
        
        
        cycle_len
        
        N %= cycle_len
        
        1 ^ 1 = 0
        1 ^ 0 = 0
        1 ^ 0 = 1
        
        cells[i] ^ cells[i+1] ^ 1
        
        """
        seen = {}
        while N:
            seen[str(cells)] = N
            N -= 1
            cells = [0] + [cells[i - 1] ^ cells[i + 1] ^ 1 for i in range(1, 7)] + [0]
            if str(cells) in seen:
                cycle_len = seen[str(cells)] - N
                N = N % cycle_len 
        return cells
            
        
                
            