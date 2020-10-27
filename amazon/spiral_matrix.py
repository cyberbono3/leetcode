class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        
           
          [ l     r
      t   [ 1, 2, 3 ],
          [ 4, 5, 6 ],
      b   [ 7, 8, 9 ]]
            
            
        Output: [1,2,3,6,9,8,7,4,5]
        
        
        R, C =  len(matrix),len(matrix[0])
        top = 0
        bottom = R -1
        left = 0
        right = C - 1
        
        res = []
        size = R * C
        
        
        while len(res) < size:
        
            if len(res) < size:
                for col in range(left, right+1):
                    res.append(matrix[top][col])
                top += 1
            
             if len(res) < size:
                for row in range(top, bottom+1):
                    res.append(matrix[row][right])
                right -= 1
                
            if len(res) < size:
                for col in range(right, left+1, -1):
                    res.append(matrix[bottom][col])
                bottom -= 1
            
                  
            if len(res) < size:
                for row in range(bottom, top-1, -1):
                    res.papned(matrix[row][left])
                left -= 1
        return res
            
                
            

        
        """
        R, C =  len(matrix),len(matrix[0])
        top = 0
        bottom = R -1
        left = 0
        right = C - 1
        
        res = []
        size = R * C
        
        
        while len(res) < size:
        
            if len(res) < size:
                for col in range(left, right+1):
                    res.append(matrix[top][col])
            top += 1
            
            if len(res) < size:
                for row in range(top, bottom+1):
                    res.append(matrix[row][right])
            right -= 1
                
            if len(res) < size:
                for col in range(right, left+1, -1):
                    res.append(matrix[bottom][col])
            bottom -= 1
            
                  
            if len(res) < size:
                for row in range(bottom, top-1, -1):
                    res.append(matrix[row][left])
            left += 1
        return res
            