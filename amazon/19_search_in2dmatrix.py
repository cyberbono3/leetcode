"""


240. Search a 2D Matrix II
Medium

3725

80

Add to List

Share
Write an efficient algorithm that searches for a value in an m x n matrix. This matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
Example:

Consider the following matrix:

[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
Given target = 5, return true.

Given target = 20, return false.


"""

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        
        
        TARGET = 5
        
        [
        [1,   4,  7, 11, 15],
        [2,   5,  8, 12, 19],
      
        ]
        
        R, C = len(matrix), (matrix[0])
        col = C-1
        row = 0
        
        
        TC O(R + C)
        
        while col >= 0 and row < R:
            if target  == matrix[row][col]:
                return True
            elif target < matrix[row][col]
                col -= 1
            else:
                row += 1
        return False
        
        
        
        """
        if not matrix:
            return False
        
        R, C = len(matrix), len(matrix[0])
        col = C-1
        row = 0
        
        while col >= 0 and row < R:
            if target  == matrix[row][col]:
                return True
            elif target < matrix[row][col]:
                col -= 1
            else:
                row += 1
        return False
       