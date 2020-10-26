class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        
        
        first is transpose the matrix and then 
                      0,1
         matrix = [[1,2,3],         [ [1, 4, 7],             [ [7, 4,1]           
                   [4,5,6],     =<    [2, 5 , 8]      =  >      [8,5,2]
                   [7,8,9]]            [3, 6, 9]]               [9, 6, 3]]
                   
        first transpose matrix and then reverse every row 
        
        
        """
        # transpose the matrix
        for i in range(len(matrix)):
            for j in range(i, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        #for every row reverse it inplace
        
        for i in range(len(matrix)):
            matrix[i].reverse()
        
        return matrix
        
        